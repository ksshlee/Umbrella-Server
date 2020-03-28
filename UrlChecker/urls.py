from django.urls import path
from UrlChecker import views


urlpatterns = [
    path('index', views.index),
    path('url', views.valid_url),
]