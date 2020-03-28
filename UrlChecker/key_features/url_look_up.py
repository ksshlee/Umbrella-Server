from datetime import datetime

import whois

def url_look_up(url):
    data = whois.whois(url)
    domain_name = data['domain_name']
    creation_date = data['creation_date']
    try:
        organization = data['org']
    except KeyError:
        organization = None

    # TODO : 만약 url 형태가 아니여서 whois 예외처리

    result = {'domain_name': domain_name, 'creation_date': creation_date, 'organization': organization}

    return result