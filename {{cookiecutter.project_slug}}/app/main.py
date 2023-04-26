# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Description: FastAPI OpenAPI Broker : main
# Date : {{cookiecutter.today}}
# Author: {{cookiecutter.full_name}} - {{cookiecutter.email}}
# ---------------------------------------------------------------------------------------------------------------------------------------------------
import uvicorn
from fastapi import FastAPI
from app.api.api_v1 import api
from app.core.config.config import settings
from app.database.connection import DbClass
from starlette.middleware.cors import CORSMiddleware


# create_app -------------------------------------------------------------------------------------------------------------------------------------------------------------
# FAST API 객체 생성 및 초기화 스크립트
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create_app():
    # 1) FastAPI 객체
    app_obj = FastAPI(
        title="{{cookiecutter.project_name}}",
        description="{{cookiecutter.project_description}}",
        version="0.9.0",
        contact={
            "name": "{{cookiecutter.full_name}}",
            "email": "{{cookiecutter.email}}"
        }
    )

    # 2) 데이터베이스 초기화
    dict_conf = dict(settings)
    DbClass.init_db(app_obj, **dict_conf)

    # 3) Celery App / Redis 정의

    # 4) 미들웨어 정의
    origins = [
        "*"
    ]
    # 개발용으로 전체 URL 허용
    app_obj.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # 5) 라우터 정의
    app_obj.include_router(api.api_router)

    return app_obj


# 메인 객체 생성
app = create_app()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Entry Point: 서버 자동 실행
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("app.main:app", port=8080, reload=True, log_level="info",  host="0.0.0.0")
