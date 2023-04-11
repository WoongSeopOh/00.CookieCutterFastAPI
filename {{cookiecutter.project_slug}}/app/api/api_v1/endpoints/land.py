# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 필지관련 OpenAPI 정보
# Date : 2023-03-16
# Author: WoongSeopOh(wsoh@vng.kr)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
import datetime
import requests
import xmltodict
from typing import Optional
from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from app.database.connection import DbClass

from app.crud import land_crud
from app.core.config import api_config
from app.schemas import land_schema


# 라우터 정의
router = APIRouter()

# 환경변수에서 가져옴
key = api_config.DATA_GO_KR_KEY
rows = api_config.NUM_OF_ROWS

# 과밀억제권역 코드
OVER_CRWD_CODE = 'UBA100'


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 과밀억제권역인지 판단하여 리턴 : ['response']['fields']['field']  / prposAreaDstrcCode == 'UBA100'
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def is_over_crwd(arg_list: list) -> str:
    for lst in arg_list:
        if lst['prposAreaDstrcCode'] == OVER_CRWD_CODE:
            return '1'

    return '0'


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 토지(임야) 대장 ['response']['fields']['field']
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@router.get("/info/{pnu}", response_model=land_schema.LandInfo, name="토지(임야)대장 조회")
def get_landinfo_by_pnu(pnu: str):
    url = api_config.LAND_INFO_URL
    params = {'serviceKey': key, 'pnu': pnu, 'numOfRows': rows}
    response = requests.get(url, params=params)

    dict_content = xmltodict.parse(response.content)

    # Todo: check Error
    cnt = dict_content['fields']['totalCount']
    if int(cnt) > 0:
        # 한건이거나 없거나
        return dict_content['fields']['ladfrlVOList']
    else:
        return ''


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 개별공시지가 목록(연도별)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@router.get("/price/{pnu}", response_model=land_schema.LandPriceList, name="개별 공시지가 조회")
def get_landprice_by_pnu(pnu: str,
                         stdryear: str = Query(default=None)):
    rtn_value = []
    url = api_config.LAND_PRICE_URL
    if stdryear is None:
        params = {'serviceKey': key, 'pnu': pnu, 'numOfRows': rows}
    else:
        params = {'serviceKey': key, 'pnu': pnu, 'numOfRows': rows, 'stdrYear': stdryear}

    response = requests.get(url, params=params)
    dict_content = xmltodict.parse(response.content)

    cnt = dict_content['response']['totalCount']
    if int(cnt) > 0:
        # 한 개일때와 여러개일때가 리턴 타입이 서로 다름.
        if int(cnt) == 1:
            rtn_value.append(dict_content['response']['fields']['field'])
        else:
            rtn_value = dict_content['response']['fields']['field']

    return {
        'totalCnt': len(rtn_value),
        'rtnList': rtn_value
    }


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 표준지 공시지가 목록(연도별)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@router.get("/pricestd/{bjdcd},{stdrYear}", response_model=land_schema.LandPriceStdList, name="표준지 공시지가 조회")
def get_landprice_std_by_pnu(bjdcd: str,
                             stdryear: str = Query(alias="공시지가 기준년도", regex='\d{4}')):
    rtn_value = []
    url = api_config.LAND_PRICE_STD_URL
    params = {'serviceKey': key, 'ldCode': bjdcd, 'stdrYear': stdryear, 'numOfRows': rows}

    response = requests.get(url, params=params)
    dict_content = xmltodict.parse(response.content)

    cnt = dict_content['response']['totalCount']
    if int(cnt) > 0:
        # 한 개일때와 여러개일때가 리턴 타입이 서로 다름.
        if int(cnt) == 1:
            rtn_value.append(dict_content['response']['fields']['field'])
        else:
            rtn_value = dict_content['response']['fields']['field']

    return {
        'totalCnt': len(rtn_value),
        'rtnList': rtn_value
    }


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 개별주택가격 정보 서비스
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@router.get("/pricehouse/{pnu},{stdryear}", response_model=land_schema.LandPriceStdList, name="개별주택가격 조회")
def get_landprice_house_by_pnu(pnu: str = Query(alias="토지고유번호", regex='\d{19}'),
                               stdryear: str = Query(alias="주택가격 기준년도", regex='\d{4}')):
    rtn_value = []
    url = api_config.LAND_PRICE_HOUSE_URL
    params = {'serviceKey': key, 'pnu': pnu, 'stdrYear': stdryear, 'numOfRows': rows}

    response = requests.get(url, params=params)
    dict_content = xmltodict.parse(response.content)

    cnt = dict_content['response']['totalCount']
    if int(cnt) > 0:
        # 한 개일때와 여러개일때가 리턴 타입이 서로 다름.
        if int(cnt) == 1:
            rtn_value.append(dict_content['response']['fields']['field'])
        else:
            rtn_value = dict_content['response']['fields']['field']

    return {
        'totalCnt': len(rtn_value),
        'rtnList': rtn_value
    }


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 토지이용계획 정보
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@router.get("/use/{pnu}", response_model=land_schema.LandUseList, name="토지이용계획 조회")
def get_landuse_by_pnu(pnu: str):
    rtn_value = []
    url = api_config.LAND_USE_URL
    params = {'serviceKey': key, 'pnu': pnu, 'numOfRows': rows}
    response = requests.get(url, params=params)

    dict_content = xmltodict.parse(response.content)

    cnt = dict_content['response']['totalCount']
    if int(cnt) > 0:
        if int(cnt) == 1:
            # 한 건인 경우 dictionay 리턴
            rtn_value.append(dict_content['response']['fields']['field'])
        else:
            # 여러 건인 경우 list 리턴
            rtn_value = dict_content['response']['fields']['field']

    return {
        'totalCnt': len(rtn_value),
        'rtnList': rtn_value
    }


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 과밀억제권역 여부 확인 1: True, 0: False
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@router.get("/overcrwd/{pnu}", response_model=land_schema.OverCrwd, name="과밀억제권역 판단")
def get_yn_overcrwd(pnu: str):
    rtn_value = []
    url = api_config.LAND_USE_URL
    params = {'serviceKey': key, 'pnu': pnu, 'numOfRows': rows}
    response = requests.get(url, params=params)

    dict_content = xmltodict.parse(response.content)

    cnt = dict_content['response']['totalCount']
    if int(cnt) > 0:
        if int(cnt) == 1:
            # 한 건인 경우 dictionay 리턴
            rtn_value.append(dict_content['response']['fields']['field'])
        else:
            # 여러 건인 경우 list 리턴
            rtn_value = dict_content['response']['fields']['field']

    return {'overCrwd': is_over_crwd(rtn_value)}


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 조정지역 여부 쿼리.. 해당 주소가 해당 시점에 조정지역이었는지 여부 확인  // 1: True, 0: False
# 옵션 파라미터의 경우 4129000000?ymd=20230327 형식으로 붙어서 날라옴..
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@router.get("/ajstrgn/{bjdcd}", response_model=land_schema.AjstRgn, name="주소기반 조정지역 여부 확인")
def get_yn_ajstrgn(bjdcd: str,
                   ymd: Optional[str] = Query(default=str(datetime.datetime.now().strftime("%Y%m%d"))),
                   db: Session = Depends(DbClass.session)):
    rtn_value = land_crud.get_yn_ajstrgn(bjdcd, ymd, db)

    return {'ajstRgn': rtn_value}
