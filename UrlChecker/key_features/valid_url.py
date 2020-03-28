from ..models import Urldata
from django.core.exceptions import ObjectDoesNotExist

def valid(result):
    domain_name_result = result['domain_name']
    creation_date = result['creation_date']
    organization = result['organization']

    if isinstance(domain_name_result, list):
        domain_name_result = domain_name_result[0]

    # 존재 하지 않을때 예외 처리
    try:
        # Upper 필수
        # upper 로 모두 대문자화
        db_result = Urldata.objects.get(domain_name=domain_name_result.upper())# 해당 db 값으로 불러오기
    except ObjectDoesNotExist:
        return False


    # 검증
    # 생성날짜가 list 일 경우
    #  2개 비교해서 하나라도 일치하면 true
    if isinstance(creation_date, list):
        print(creation_date[0] == db_result.creation_date)
        if creation_date[0] == db_result.creation_date or creation_date[1] == db_result.creation_date:
            # organization 이 둘다 none 이 아닐 경우
            if organization is not None and db_result.organization is not None:
                if organization == db_result.organization:
                    return True
    else:
        if creation_date == db_result.creation_date:
            if organization is not None and db_result.organization is not None:
                if organization == db_result.organization:
                    return True


    return False
