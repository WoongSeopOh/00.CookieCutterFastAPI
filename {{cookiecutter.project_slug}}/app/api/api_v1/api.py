# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Description: Version 1 전체 라우팅 정보
# Date : {cookiecutter.today}}
# Author: {cookiecutter.full_name}} - {cookiecutter.email}}  
# ---------------------------------------------------------------------------------------------------------------------------------------------------
from fastapi import APIRouter
from app.api.api_v1.endpoints import land

api_router = APIRouter(
    prefix="/api/v1"
)
api_router.include_router(land.router, prefix="/land", tags=["일필지 정보"])
