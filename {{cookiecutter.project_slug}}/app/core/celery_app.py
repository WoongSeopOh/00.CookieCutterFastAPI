# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 비동기 처리를 위한 Celery App 정의
# Date : {{cookiecutter.today}}
# Author: {{cookiecutter.full_name}} - {{cookiecutter.email}}
# ---------------------------------------------------------------------------------------------------------------------------------------------------
from celery import Celery
from app.core.config import celery_config

# Celery 인스턴스 생성 : redis 서버 지정
# Note 실행 celery -A main.celery worker --loglevel=info --pool=solo
#          flower 같이 실행시 별도의 터미널로 실행해야 함.

celery_app = Celery(
    'celery_app',
    broker=celery_config.broker_url,
    backend=celery_config.result_backend,
    include=['celery_worker']
)

# rabbitMQ 사용시
# celery_task = Celery(
#     __name__,
#     broker="amqp://guest:guest@192.168.0.10:5672",
# )

# endpoint에서 사용하는 함수 예제

# @app.get("/work")
# async def work(task_id: str, input_a: int, input_b: int):
#     divide.apply_async([input_a, input_b], task_id=task_id)
#     return {"message": "celery start"}

# @app.get("/work_result")
# async def work_result(task_id: str):
#     result = divide.AsyncResult(task_id)
#     return {"message": result.info}


def task(acks_late):
    return None
