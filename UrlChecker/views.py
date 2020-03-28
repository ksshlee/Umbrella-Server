from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Urldata
from .forms import UrlForm
from .key_features.url_look_up import url_look_up
from .key_features.valid_url import valid
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def valid_url(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        url = form.data['url'] # form 에서 url 추출
        results = url_look_up(url) # url whois 로 조회 결과 results에 담기

        if valid(results):
            return HttpResponse('<h1>통과</h1>')
        else :
            return HttpResponse('<h1>실패</h1')