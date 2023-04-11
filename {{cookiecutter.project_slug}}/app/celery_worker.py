# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 비동기로 처리해야하는 작업 정의
# Date : {cookiecutter.today}}
# Author: {cookiecutter.full_name}} - {cookiecutter.email}}  
# ---------------------------------------------------------------------------------------------------------------------------------------------------
from app.core import celery_app
import time


@celery_app.task
def test_divide(x: int, y: int):
    time.sleep(5)
    return x / y
