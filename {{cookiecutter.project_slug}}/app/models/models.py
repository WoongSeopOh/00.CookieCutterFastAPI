# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 사용하는 모델을 정의
# Date : 2023-03-23
# Author: WoongSeopOh(wsoh@vng.kr)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
import datetime
from sqlalchemy import Column, Integer, String, Numeric, Text, DateTime, ForeignKey
from app.database.connection import Base
from sqlalchemy.orm import relationship


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 조정지역 모델 클래스 정의
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class AjstRgnInfo(Base):
    __tablename__ = "ajst_rgn_info"
    __table_args__ = {"comment": "조정지역"}

    ajst_rgn_sn = Column(Integer, autoincrement=True, primary_key=True, nullable=False, comment="조정지역일련번호")
    bgnde = Column(String(8), nullable=False, comment="시작일자")
    endde = Column(String(8), nullable=False, comment="종료일자", default="99991231")
    bjd_code = Column(String(10), nullable=False, comment="법정동코드")
    ctprvn_nm = Column(String(64), comment="시도명")
    sigungu_nm = Column(String(64), comment="시군구명")
    emd_nm = Column(String(64), comment="읍면동명")
    dongli_nm = Column(String(64), comment="리명")
    regist_dt = Column(String(14), nullable=False, comment="등록일시", default=str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 실거래가 모델 클래스 정의
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class AptRealPrice(Base):
    __tablename__ = "apt_realprice_info"
    __table_args__ = {"comment": "실거래가"}

    deal_prce_sn = Column(Integer, autoincrement=True, primary_key=True, nullable=False, comment="실거래가일련번호")
    deal_de = Column(String(8), comment="거래일")
    pnu = Column(String(19), comment="토지고유번호")
    apt_nm = Column(String(64), comment="아파트명")
    floor = Column(String(4), comment="층")
    prvuse_ar = Column(String(20), comment="전용면적")
    deal_amount = Column(String(40), comment="거래금액")
    bldg_yr = Column(String(4), comment="건축년도")
    clr_occur_de = Column(String(8), comment="해제사유발생일")
    clr_at = Column(String(1), comment="해제여부")
    rd_sgg_code = Column(String(5), comment="도로명시군구코드")
    rdnm_code = Column(String(7), comment="도로명코드")
    rdnm = Column(String(40), comment="도로명")
    rd_fr_code = Column(String(1), comment="도로명지상지하코드")
    rd_main_no = Column(String(5), comment="도로명건물본번호코드")
    rd_sub_no = Column(String(5), comment="도로명건물부번호코드")
    regist_dt = Column(String(14), nullable=False, comment="등록일시", default=str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 전국법정동코드 모델 클래스 정의
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class AdminJsCode(Base):
    __tablename__ = "admin_js_code"
    __table_args__ = {"comment": "전국법정동코드"}

    bjd_code = Column(String(10), nullable=False, primary_key=True, comment="법정동코드")
    ctprvn_nm = Column(String(64), nullable=False, comment="시도명")
    sigungu_nm = Column(String(64), comment="시군구명")
    emd_nm = Column(String(64), comment="읍명동명")
    dongli_nm = Column(String(64), comment="동리명")
    creat_de = Column(String(8), comment="생성일자")
    delete_de = Column(String(8), comment="말소일자")
    regist_dt = Column(String(14), nullable=False, comment="등록일시", default=str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
