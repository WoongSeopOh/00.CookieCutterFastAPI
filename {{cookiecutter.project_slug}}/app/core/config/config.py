# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 로컬/개발/운영에 따른 변하는 환경 구성 파일 (아래 종류의 정보들)
#              API keys to access third-party services
#              Passwords and credentials
#              Email addresses or personal data (name, age, social security number, etc.)
#              Debug flags
#              Hosts, URL, URI
# Date : {{cookiecutter.today}}
# Author: {{cookiecutter.full_name}} - {{cookiecutter.email}}
# ---------------------------------------------------------------------------------------------------------------------------------------------------
from typing import Optional
from pydantic import BaseSettings, PostgresDsn


# GlobalSettings -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 공통 셋팅 정보 관리
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
class GlobalSettings(BaseSettings):
    # TODO: 향후에 정확한 환경변수 설정을 통해서 로컬, 개발환경, 운영환경을 구분한다.
    ENV_STATE: str = 'tempState'

    API_VERSION: str = "/api/v1"

    # 데이터베이스 관련 정보
    BASE_DIR: str = None
    # local
    DB_CON_STRING: PostgresDsn = 'postgresql+psycopg2://{{cookiecutter.db_user_name}}:{{cookiecutter.db_password}}@{{cookiecutter.db_url}}:{{cookiecutter.db_port}}/{{cookiecutter.db_name}}'
    # prod
    # DB_CON_STRING: PostgresDsn = 'postgresql+psycopg2://fastapi:fastapi@172.17.0.3:5432/db_fastapi'
    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True

    # .env 파일 정의 (APP_ENV 값은 .env 파일에 정의됨)
    class Config:
        env_file = '.env'


# DevSettings -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 개발환경에 특화된 셋팅 정보
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
class DevSettings(GlobalSettings):
    class Config:
        env_file = 'dev.env'


# ProdSettings -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 운영환경에 특화된 셋팅 정보
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
class ProdSettings(GlobalSettings):
    class Config:
        env_file = 'prod.env'


# FactorySettings -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 설치된 서버의 환경변수에 따라 해당 값을 동적으로 가져옴
#              todo: 환경변수 셋팅이 필수 (환경변수가 없으면 GlobalSettings에서 정하고 있는 .env 파일에서 가져옴)
#              Hint: .env와 환경변수에 동일한 변수가 선언되어 있다면 환경변수 설정값이 항상 우선시됨.
#              Hint: 파일에 정의된 변수와 현재 클래스 변수명이 같으면 해당 변수에 env 값이 바인딩 됨..
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
class FactorySettings:
    @staticmethod
    def load():
        # 인스턴스의 변수 (스태틱과 다름.. 괄호.. 주의!!)
        env_state = GlobalSettings().ENV_STATE
        if env_state == 'dev':
            # 인스턴스를 리턴
            return DevSettings()
        elif env_state == 'prod':
            return ProdSettings()
        else:
            return GlobalSettings()


# Hint: Static 메소드이기 때문에 인스턴스 생성없이 바로 접근
settings = FactorySettings.load()

