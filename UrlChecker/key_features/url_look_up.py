from datetime import datetime

import whois

def v1_url_look_up(url):
    # data whois 조회
    data = whois.whois(url)
    # 도메인 이름만 추출
    domain_name = data['domain_name']
    #  생성날짜 추출
    creation_date = data['creation_date']
    result = {'domain_name': domain_name, 'creation_date': creation_date}
    return result