# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Description: Celery Config 파일 정의
# Date : 2023-03-13
# Author: WoongSeopOh(wsoh@vng.kr)
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Message Server URL 정의 (Redis)
broker_url = '{{cookiecutter.redis_url}}'
result_backend = '{{cookiecutter.redis_url}}'

# broker_url = 'redis://192.168.0.10:6379/0'
# result_backend = 'redis://192.168.0.10:6379/0'

# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
# timezone = 'Asia/Seoul'
# enable_utc = True


# task_routes = {
#     'tasks.add': 'low-priority',
# }
#
# task_annotations = {
#     'tasks.add': {'rate_limit': '10/m'},
# }
