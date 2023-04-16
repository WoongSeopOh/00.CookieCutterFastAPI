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
import os
from pydantic import BaseSettings, PostgresDsn
from dotenv import load_dotenv

load_dotenv()


# GlobalSettings -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 공통 셋팅 정보 관리
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
class GlobalSettings(BaseSettings):
    FASTAPI_ENV_STATE: str = os.getenv('FASTAPI_ENV_STATE')

    API_VERSION: str = "/api/v1"

    # 데이터베이스 관련 정보
    BASE_DIR: str = None
    DB_ECHO: bool = True
    DB_POOL_RECYCLE: int = 900


# DevSettings -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 개발환경에 특화된 셋팅 정보
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
class LocalSettings(GlobalSettings):
    DB_CON_STRING: PostgresDsn = "postgresql+psycopg2://forest:forest@demo.vng.co.kr:59401/forest"

    class Config:
        env_file = 'local.env'


# ProdSettings -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 운영환경에 특화된 셋팅 정보
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
class ProdSettings(GlobalSettings):
    DB_CON_STRING: PostgresDsn = "postgresql+psycopg2://forest:forest@demo.vng.co.kr:59402/forest"

    class Config:
        env_file = 'prod.env'


# FactorySettings -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 설치된 서버의 환경변수에 따라 해당 값을 동적으로 가져옴
#              Hint: .env와 환경변수에 동일한 변수가 선언되어 있다면 환경변수 설정값이 항상 우선시됨.
#              Hint: .env file에 정의한 내용은 os.getenv('key') 형식으로 접근한다.
#              Hint: 파일에 정의된 변수와 현재 클래스 변수명이 같으면 해당 변수에 env 값이 바인딩 됨..
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
class FactorySettings:
    @staticmethod
    def load():
        # 인스턴스의 변수 (스태틱과 다름.. 괄호.. 주의!!)
        env_state = GlobalSettings().FASTAPI_ENV_STATE
        if env_state == 'local':
            return LocalSettings()
        elif env_state == 'prod':
            return ProdSettings()
        else:
            return GlobalSettings()


# Hint: Static 메소드이기 때문에 인스턴스 생성없이 바로 접근
settings = FactorySettings.load()

