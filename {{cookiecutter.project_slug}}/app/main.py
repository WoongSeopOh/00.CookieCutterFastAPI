# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Description: FastAPI OpenAPI Broker : main
# Date : 2023-03-08
# Author: WoongSeopOh(wsoh@vng.kr)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
import uvicorn
from fastapi import FastAPI
from app.api.api_v1 import api
from dataclasses import asdict
from app.core.config.config import settings
from app.database.connection import DbClass


# create_app -------------------------------------------------------------------------------------------------------------------------------------------------------------
# FAST API 객체 생성 및 초기화 스크립트
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create_app():
    # 1) FastAPI 객체
    app_obj = FastAPI(
        title="미래전략사업팀 공용 OpenAPI Service",
        description="공개된 OpenAPI 서비스를 하나의 Broker 서비스로 구성하여 여러 프로젝트에서 활용 예정",
        version="0.9.0",
        contact={
            "name": "WoongSeopOh(Patrick)",
            "email": "wsoh@vng.kr"
        }
    )

    # 2) 데이터베이스 초기화
    dict_conf = dict(settings)
    DbClass.init_db(app_obj, **dict_conf)

    # 3) Celery App / Redis 정의

    # 4) 미들웨어 정의
    # origins = [
    #     "http://127.0.0.1:5173"
    # ]
    # fastapi_obj.add_middleware(
    #     CORSMiddleware,
    #     allow_orgins=origins,
    #     allow_credentials=True,
    #     allow_method=["*"],
    #     allow_headers=["*"],
    # )

    # 5) 라우터 정의
    app_obj.include_router(api.api_router)

    return app_obj


# 메인 객체 생성
app = create_app()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Entry Point: 서버 자동 실행
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True, log_level="info")