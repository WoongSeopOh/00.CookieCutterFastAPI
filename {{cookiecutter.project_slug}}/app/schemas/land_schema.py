# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Description: 필지 정보에 대한 스키마
# Date : {cookiecutter.today}}
# Author: {cookiecutter.full_name}} - {cookiecutter.email}}  
# ---------------------------------------------------------------------------------------------------------------------------------------------------
from typing import Optional
from pydantic import BaseModel, Field


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 토지/임야 대장
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class LandInfo(BaseModel):
    ldCodeNm: Optional[str] = Field(title='법정동명', description='토지가 소재한 소재지의 행정구역코드(법정동코드) 10자리', default=None)
    mnnmSlno: Optional[str] = Field(title='지번', description='필지에 부여하여 지적공부에 등록한 번호', default=None)
    lndcgrCodeNm: Optional[str] = Field(title='지목명', description='코드 정보', default=None)
    lndpclAr: Optional[str] = Field(title='면적(㎡)', description='지적공부에 등록한 필지의 수평면상 넓이(㎡)', default=None)
    posesnSeCodeNm: Optional[str] = Field(title='소유구분명', description='코드 정보', default=None)
    cnrsPsnCo: Optional[str] = Field(title='소유(공유)인수(명)', description='토지를 공동 소유하고있는 사람수(명)', default=None)

    # 전체 리턴정보 목록
    # pnu: Optional[str] = Field(title='고유번호', description='각 필지를 서로 구별하기 위하여 필지마다 붙이는 고유한 번호', default=None)
    # ldCode: Optional[str] = Field(title='법정동코드', description='토지가 소재한 소재지의 행정구역 명칭(법정동명)', default=None)
    # regstrSeCode: Optional[str] = Field(title='대장구분코드', description='토지가 위치한 토지의 대장 구분 (토지(임야)대장구분)코드', default=None)
    # regstrSeCodeNm: Optional[str] = Field(title='대장구분명', description='코드 정보', default=None)
    # lndcgrCode: Optional[str] = Field(title='지목코드', description='토지의 주된 용도에 따라 토지의 종류를 구분한 지목코드', default=None)
    # posesnSeCode: Optional[str] = Field(title='소유구분코드', description='국토를 토지 소유권 취득 주체에 따라 구분한 코드', default=None)
    # ladFrtlSc: Optional[str] = Field(title='축척구분코드', description='토지(임야)대장에 등록된 지적도(임야도)의 축척구분 코드', default=None)
    # ladFrtlScNm: Optional[str] = Field(title='축척구분명', description='코드 정보', default=None)
    # lastUpdtDt: Optional[str] = Field(title='데이터기준일자', description='데이터 작성 기준일자', default=None)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 개별공시지가
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class LandPrice(BaseModel):
    ldCodeNm: Optional[str] = Field(title='법정동명', description='토지가 소재한 소재지의 행정구역 명칭(법정동명)', default=None)
    regstrSeCodeNm: Optional[str] = Field(title='특수지구분명', description='해당 필지의 특수지 구분 명', default=None)
    mnnmSlno: Optional[str] = Field(title='지번', description='필지에 부여하여 지적공부에 등록한 번호', default=None)
    stdrYear: Optional[str] = Field(title='기준년도', description='개별공시지가의 기준년도', default=None)
    stdrMt: Optional[str] = Field(title='기준월', description='개별공시지가의 기준월', default=None)
    pblntfPclnd: Optional[str] = Field(title='공시지가(원/㎡)', description='개별토지에한 공시가격(원/㎡)', default=None)
    pblntfDe: Optional[str] = Field(title='공시일자', description='개별공시지가의 공시년월일', default=None)
    stdLandAt: Optional[str] = Field(title='표준지여부(Y/N)', description='대상 토지를 평가할 때, 평가의 기준으로 삼는 필지의 여부 (Y/N)', default=None)

    # 전체 리턴정보 목록
    # pnu: Optional[str] = Field(title='고유번호', description='각 필지를 서로 구별하기 위하여 필지마다 붙이는 고유한 번호', default=None)
    # ldCode: Optional[str] = Field(title='법정동코드', description='토지가 소재한 행정구역코드(법정동코드) 10자리', default=None)
    # regstrSeCode: Optional[str] = Field(title='특수지구분코드', description='해당 필지의 특수지 코드', default=None)
    # lastUpdtDt: Optional[str] = Field(title='데이터기준일자', description='데이터 작성 기준일자', default=None)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 연도별 개별공시지가 : 특정 필지의 연도별 공시지가 리스트
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class LandPriceList(BaseModel):
    totalCnt: int = 0
    rtnList: list[LandPrice] = []


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 표준지 공시지가
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class LandPriceStd(BaseModel):
    pnu: Optional[str] = Field(title='고유번호', description='고유번호', default=None)
    ldCodeNm: Optional[str] = Field(title='법정동명', description='법정동명', default=None)
    mnnmSlno: Optional[str] = Field(title='지번', description='지번', default=None)
    stdrYear: Optional[str] = Field(title='기준년도', description='기준년도', default=None)
    lndcgrCodeNm: Optional[str] = Field(title='지목', description='지목', default=None)
    cnflcRt: Optional[str] = Field(title='저촉율(%)', description='저촉율(%)', default=None)
    ladUseSittnNm: Optional[str] = Field(title='토지이용상황', description='토지이용상황', default=None)
    tpgrphHgCodeNm: Optional[str] = Field(title='지형높이(m)', description='지형높이(m)', default=None)
    tpgrphFrmCodeNm: Optional[str] = Field(title='지형형상', description='지형형상', default=None)
    roadSideCodeNm: Optional[str] = Field(title='도로측면', description='도로측면', default=None)
    roadDstncCodeNm: Optional[str] = Field(title='도로거리', description='도로거리', default=None)
    pblntfPclnd: Optional[str] = Field(title='공시지가(원/㎡)', description='공시지가(원/㎡)', default=None)
    lndpclAr: Optional[str] = Field(title='토지면적(㎡)', description='토지면적(㎡)', default=None)

    # 전체 리턴 목록
    # ldCode: Optional[str] = Field(title='법정동코드', description='법정동코드', default=None)
    # regstrSeCode: Optional[str] = Field(title='특수지구분코드', description='특수지구분코드', default=None)
    # regstrSeCodeNm: Optional[str] = Field(title='특수지구분명', description='특수지구분명', default=None)
    # stdLandSn: Optional[str] = Field(title='표준지일련번호', description='표준지일련번호', default=None)
    # bsnsDstrcAr: Optional[str] = Field(title='사업지구면적(㎡)', description='사업지구면적(㎡)', default=None)
    # lndcgrCode: Optional[str] = Field(title='지목코드', description='지목코드', default=None)
    # prposArea1: Optional[str] = Field(title='용도지역코드1', description='용도지역코드1', default=None)
    # prposAreaNm1: Optional[str] = Field(title='용도지역명1', description='용도지역명1', default=None)
    # prposArea2: Optional[str] = Field(title='용도지역코드2', description='용도지역코드2', default=None)
    # prposAreaNm2: Optional[str] = Field(title='용도지역명2', description='용도지역명2', default=None)
    # prposDstrc1: Optional[str] = Field(title='용도지구코드1', description='용도지구코드1', default=None)
    # prposDstrcNm1: Optional[str] = Field(title='용도지구명1', description='용도지구명1', default=None)
    # prposDstrc2: Optional[str] = Field(title='용도지구코드2', description='용도지구코드2', default=None)
    # prposDstrcNm2: Optional[str] = Field(title='용도지구명2', description='용도지구명2', default=None)
    # ladUseSittn: Optional[str] = Field(title='토지이용상황코드', description='토지이용상황코드', default=None)
    # tpgrphHgCode: Optional[str] = Field(title='지형높이코드', description='지형높이코드', default=None)
    # tpgrphFrmCode: Optional[str] = Field(title='지형형상코드', description='지형형상코드', default=None)
    # roadSideCode: Optional[str] = Field(title='도로측면코드', description='도로측면코드', default=None)
    # roadDstncCode: Optional[str] = Field(title='도로거리코드', description='도로거리코드', default=None)
    # stdlandPosesnSeCode: Optional[str] = Field(title='표준지소유구분코드', description='표준지소유구분코드', default=None)
    # stdlandPosesnSeCodeNm: Optional[str] = Field(title='표준지소유구분명', description='표준지소유구분명', default=None)
    # posesnStle: Optional[str] = Field(title='소유형태코드', description='소유형태코드', default=None)
    # posesnStleNm: Optional[str] = Field(title='소유형태명', description='소유형태명', default=None)
    # lastUpdtDt: Optional[str] = Field(title='데이터기준일자', description='데이터기준일자', default=None)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 표준지 공시지가리스트 (법정읍면동 단위로 목록 생성됨)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class LandPriceStdList(BaseModel):
    totalCnt: int = 0
    rtnList: list[LandPriceStd] = []


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 토지이용계획정보 : 일필지 기준
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class LandUse(BaseModel):
    ldCodeNm: Optional[str] = Field(title='법정동명', description='토지가 소재한 소재지의 행정구역 명칭(법정동명)', default=None)
    mnnmSlno: Optional[str] = Field(title='지번', description='필지에 부여하여 지적공부에 등록한 번호', default=None)
    cnflcAtNm: Optional[str] = Field(title='저촉여부', description='저촉여부', default=None)
    cnflcAt: Optional[str] = Field(title='저촉여부코드', description='저촉여부를 나타내는 번호', default=None)
    prposAreaDstrcCode: Optional[str] = Field(title='용도지역지구코드', description='용도지역지구코드', default=None)
    prposAreaDstrcCodeNm: Optional[str] = Field(title='용도지역지구명', description='용도지역지구명', default=None)
    registDt: Optional[str] = Field(title='등록일자', description='등록일자', default=None)

    # 전체 리턴정보 목록
    # pnu: Optional[str] = Field(title='고유번호', description='각 필지를 서로 구별하기 위하여 필지마다 붙이는 고유한 번호', default=None)
    # ldCode: Optional[str] = Field(title='법정동코드', description='토지가 소재한 행정구역코드(법정동코드) 10자리', default=None)
    # regstrSeCode: Optional[str] = Field(title='대장구분코드', description='토지가 위치한 토지의 대장 구분(토지(임야)대장구분)코드', default=None)
    # regstrSeCodeNm: Optional[str] = Field(title='대장구분명', description='토지가 위치한 토지의 대장 구분 (토지(임야)대장구분)', default=None)
    # manageNo: Optional[str] = Field(title='도면번호', description='지적 도면의 번호', default=None)

    # lastUpdtDt: Optional[str] = Field(title='데이터기준일자', description='데이터 작성 기준일자', default=None)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 과밀억제권역 판단
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class OverCrwd(BaseModel):
    overCrwd: Optional[str] = Field(title='과밀억제권역여부', description='과밀억제권역인지에 따라 True/False 반환', default='0')


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 토지이용계획서비스 목록
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class LandUseList(BaseModel):
    totalCnt: int = 0
    rtnList: list[LandUse] = []


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 개별주택가격
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class LandPriceHouse(BaseModel):
    pnu: Optional[str] = Field(title='고유번호', description='고유번호', default=None)
    ldCodeNm: Optional[str] = Field(title='법정동명', description='법정동명', default=None)
    mnnmSlno: Optional[str] = Field(title='지번', description='지번', default=None)
    stdrYear: Optional[str] = Field(title='기준년도', description='기준년도', default=None)
    stdrMt: Optional[str] = Field(title='기준월', description='기준월', default=None)
    ladRegstrAr: Optional[str] = Field(title='토지대장면적(㎡)', description='토지대장면적(㎡)', default=None)
    calcPlotAr: Optional[str] = Field(title='산정대지면적(㎡)', description='산정대지면적(㎡)', default=None)
    buldAllTotAr: Optional[str] = Field(title='건물전체연면적(㎡)', description='건물전체연면적(㎡)', default=None)
    buldCalcTotAr: Optional[str] = Field(title='건물산정연면적(㎡)', description='건물산정연면적(㎡)', default=None)
    housePc: Optional[str] = Field(title='주택가격(원)', description='주택가격(원)', default=None)
    stdLandAt: Optional[str] = Field(title='표준지여부', description='표준지여부', default=None)

    # 전체 리턴 목록
    # ldCode: Optional[str] = Field(title='법정동코드', description='법정동코드', default=None)
    # regstrSeCode: Optional[str] = Field(title='특수지구분코드', description='특수지구분코드', default=None)
    # regstrSeCodeNm: Optional[str] = Field(title='특수지구분명', description='특수지구분명', default=None)
    # bildRegstrEsntlNo: Optional[str] = Field(title='건축물대장고유번호', description='건축물대장고유번호', default=None)
    # dongCode: Optional[str] = Field(title='동코드', description='동코드', default=None)
    # lastUpdtDt: Optional[str] = Field(title='데이터기준일자', description='데이터기준일자', default=None)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 개별주택가격 목록
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class LandPriceHouseList(BaseModel):
    totalCnt: int = 0
    rtnList: list[LandPriceHouse] = []


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 조정지역 여부 판단
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class AjstRgn(BaseModel):
    ajstRgn: Optional[str] = Field(title='조정지역여부', description='조정지역 여부에 따라 True/False 반환', default='0')

