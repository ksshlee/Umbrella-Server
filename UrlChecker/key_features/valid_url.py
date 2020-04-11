from ..models import Urldata
from django.core.exceptions import ObjectDoesNotExist

def v1_valid(result):
    domain_name_result = result['domain_name']
    creation_date = result['creation_date']

    if isinstance(domain_name_result, list):
        domain_name_result = domain_name_result[0]

    # 존재 하지 않을때 예외 처리
    try:
        db_result = Urldata.objects.get(domain_name=domain_name_result.upper())# 해당 db 값으로 불러오기
    except ObjectDoesNotExist:
        result['valid'] = False
        return result


    # 검증
    # 생성날짜가 list 일 경우
    #  2개 비교해서 하나라도 일치하면 true
    if isinstance(creation_date, list):
        if creation_date[0] == db_result.creation_date or creation_date[1] == db_result.creation_date:
            result['valid'] = True
            return result
    else:
        if creation_date == db_result.creation_date:
            result['valid'] = True
            return result

    result['valid'] = False
    return result
