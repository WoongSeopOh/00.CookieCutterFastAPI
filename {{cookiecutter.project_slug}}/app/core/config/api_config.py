# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Description: OpenAPI 관련 설정 정보
# Date : {{cookiecutter.today}}
# Author: {{cookiecutter.full_name}} - {{cookiecutter.email}}
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# KAKAO API KEY
KAKAO_APP_KEY = 'KakaoAK 6377c9a823201926bdb40897dbfb035c'
KAKAO_REST_API_KEY = 'KakaoAK b9a7527966ab6bf7d18db80367b4b491'
KAKAO_JS_KEY = 'KakaoAK 3488a1501a3e7b55841d4e34ce58d0d7'
KAKAO_ADMIN_KEY = 'KakaoAK abe6b82dddff934228faacc727d8467c'
KAKAO_PAGE = 45
KAKAO_SIZE = 30

# KAKAO URL
KAKAO_ADDR_URL = 'https://dapi.kakao.com/v2/local/search/address.json'
KAKAO_KEYWORD_URL = 'https://dapi.kakao.com/v2/local/search/keyword.json'

# JUSO.GO.KR API
JUSO_KEY = 'devU01TX0FVVEgyMDIzMDMwOTE2MTQxMTExMzU3OTg='
JUSO_KEYWORD_URL = 'https://business.juso.go.kr/addrlink/addrLinkApi.do'

# 상세주소 검색 API KEY devU01TX0FVVEgyMDIzMDMxNjIwNDYxNzExMzYwMTU
JUSO_DETAIL_KEY = 'devU01TX0FVVEgyMDIzMDMxNjIwNTYzNTExMzYwMTc='
JUSO_DETAIL_URL = 'https://business.juso.go.kr/addrlink/addrDetailApi.do'

# 공공데이터포털 OpenAPI
DATA_GO_KR_KEY: str = 'RnMwF7pUHgbIDX2GzfFQ43ukfvHEZkHMWQMs5o2sCs1tq+YnaOnzHf/+CDmqWTaGcQVBwr09BgC/zWk2QzlLng=='
NUM_OF_ROWS: str = '999'

# 공동주택 단지 목록제공 서비스
APT_ROADCD_URL: str = 'http://apis.data.go.kr/1613000/AptListService2/getRoadnameAptList'
APT_SIDO_URL: str = 'http://apis.data.go.kr/1613000/AptListService2/getSidoAptList'
APT_SGG_URL: str = 'http://apis.data.go.kr/1613000/AptListService2/getSigunguAptList'
APT_TOTAL_URL: str = 'http://apis.data.go.kr/1613000/AptListService2/getTotalAptList'
APT_BJD_URL: str = 'http://apis.data.go.kr/1613000/AptListService2/getLegaldongAptList'

# 국토교통부_공동주택 기본 정보제공 서비스
APT_BASIC_URL: str = 'http://apis.data.go.kr/1613000/AptBasisInfoService1/getAphusBassInfo'
APT_DETAIL_URL: str = 'http://apis.data.go.kr/1613000/AptBasisInfoService1/getAphusDtlInfo'

# 아파트 가격정보
APT_PRICE_URL: str = 'http://apis.data.go.kr/1611000/nsdi/ApartHousingPriceService/attr/getApartHousingPriceAttr'
# 아파트 실거래가 (한글 Element ㅠ)
# APT_REAL_PRICE_URL: str = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'

# 건축물대장 서비스(총괄표제부)
BLDG_RECAP_URL: str = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrRecapTitleInfo'
# 건축물대장 서비스(표제부)
BLDG_TITLE_URL: str = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrTitleInfo'
# 건축물대장 서비스(기본개요)
BLDG_BASIC_URL: str = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrBasisOulnInfo'
# 건축물대장 서비스(층별개요)
BLDG_FLOOR_URL: str = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrFlrOulnInfo'
# 건축물대장 서비스(전유공유면적)
BLDG_EXPOSAREA_URL: str = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposPubuseAreaInfo'
# 건축물대장 서비스(주택가격)
BLDG_PRICE_URL: str = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrHsprcInfo'
# 건축물대장 서비스(전유부)
BLDG_EXPOS_URL: str = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposInfo'
# 건축물대장 서비스(지구구역정보)
BLDG_JIGU_URL: str = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrJijiguInfo'

# 토지(임야)대장
LAND_INFO_URL: str = 'http://apis.data.go.kr/1611000/nsdi/eios/LadfrlService/ladfrlList.xml'
# 개별공시지가
LAND_PRICE_URL: str = 'http://apis.data.go.kr/1611000/nsdi/IndvdLandPriceService/attr/getIndvdLandPriceAttr'
# 표준지공시지가
LAND_PRICE_STD_URL: str = 'http://apis.data.go.kr/1611000/nsdi/ReferLandPriceService/attr/getReferLandPriceAttr'
# 토지이용계획
LAND_USE_URL: str = 'http://apis.data.go.kr/1611000/nsdi/LandUseService/attr/getLandUseAttr'
# 개별주택가격
LAND_PRICE_HOUSE_URL: str = 'http://apis.data.go.kr/1611000/nsdi/IndvdHousingPriceService/attr/getIndvdHousingPriceAttr'
