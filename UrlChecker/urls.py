from django.urls import path
from UrlChecker import views


urlpatterns = [
    path('url', views.valid_url),
]