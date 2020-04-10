from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Urldata
from .forms import UrlForm
from .key_features.url_look_up import url_look_up
from .key_features.valid_url import valid
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
def valid_url(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        url = form.data['url'] # form 에서 url 추출
        # 만약 Url 이 비어있으면 url 비어있다는 에러
        if(len(url)<=0):
            return JsonResponse({'message':'url 비어있음'},status=404)
        results = url_look_up(url) # url whois 로 조회 결과 results 에 담기


    if results['domain_name'] is None:
        # url 형식이 아니라서 url 형식 맞는지 알려줘야함
        # 아니면 url 의 whois 조회가 안되는거임
        # 404
        return JsonResponse({'status':'404'},status=404)
    else :
        # False 가 아니면
        valid_result = valid(results)

        if valid_result['valid'] is False :
            #403
            return JsonResponse({'result': valid_result}, status=403)
        else:
            # 200
            return JsonResponse({'result': valid_result}, status=200)
