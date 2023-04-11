# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Description: Database 연결 (Database 연결자 앱 초기화시 생성, 싱글턴 사용)
# Date : {cookiecutter.today}}
# Author: {cookiecutter.full_name}} - {cookiecutter.email}}  
# ---------------------------------------------------------------------------------------------------------------------------------------------------
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class SQLAlchemy:
    def __init__(self, arg_app: FastAPI = None, **kwargs):
        self._engine = None
        self._session = None
        if arg_app is not None:
            self.init_db(app=arg_app, **kwargs)

    def init_db(self, app: FastAPI, **kwargs):
        db_con_string = kwargs.get("DB_CON_STRING")
        db_pool_recycle = kwargs.setdefault("DB_POOL_RECYCLE", 900)
        db_echo = kwargs.setdefault("DB_ECHO", True)

        # DB Connection 생성(Pool)
        self._engine = create_engine(db_con_string, echo=db_echo, pool_recycle=db_pool_recycle, pool_pre_ping=True)

        # 세션 메이커
        self._session = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

        # Event 등록 // App 실행시 커넥션 생성
        @app.on_event("startup")
        def startup():
            self._engine.connect()

        @app.on_event("shutdown")
        def shutdown():
            self._session.close_all()
            self._engine.dispose()

    def get_db(self):
        db_session = None
        if self._session is None:
            raise Exception("first, call init_app function")
        else:
            try:
                db_session = self._session()
                yield db_session
            finally:
                db_session.close()

    # Getter, Setter 역할 Property
    @property
    def session(self):
        return self.get_db

    @property
    def engin(self):
        return self._engine


# Singleton Pattern
DbClass = SQLAlchemy()
Base = declarative_base()
