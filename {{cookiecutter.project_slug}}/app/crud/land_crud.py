# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 일필지 정보에 대한 CRUD 구성
# Date : {{cookiecutter.today}}
# Author: {{cookiecutter.full_name}} - {{cookiecutter.email}}
# ---------------------------------------------------------------------------------------------------------------------------------------------------
from sqlalchemy.orm import Session
from app.models.models import AjstRgnInfo
from sqlalchemy import and_


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 주소 기반으로 조정지역 여부 확인  # sqlalchemy.orm.query.Query
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_yn_ajstrgn(code: str, ymd: str, db: Session) -> str:
    # filter, filter_by, get, first(), one(), fetchall(), all(), scalar()
    # result = db.query(AjstRgnInfo).filter(AjstRgnInfo.bjd_code == code).first()
    result = db.query(AjstRgnInfo).filter(and_(AjstRgnInfo.bjd_code == code,
                                               ymd >= AjstRgnInfo.bgnde,
                                               ymd <= AjstRgnInfo.endde)).first()
    if result is None:
        return '0'
    else:
        return '1'
