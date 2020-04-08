from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Urldata
from .forms import UrlForm
from .key_features.url_look_up import url_look_up
from .key_features.valid_url import valid
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def valid_url(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        url = form.data['url'] # form 에서 url 추출
        results = url_look_up(url) # url whois 로 조회 결과 results에 담기

    if results is False:
        # url 형식이 아니라서 url 형식 맞는지 알려줘야함
        # 아니면 url 의 whois 조회가 안되는거임
        # 404
        return JsonResponse({'status':'404'},status=404)
    else :
        if valid(results):
            # 200
            return JsonResponse({'status':'200'},status=200)
        else :
            # 403 에러
            return JsonResponse({'status':'403'},status=403)