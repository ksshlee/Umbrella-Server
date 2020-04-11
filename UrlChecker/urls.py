from django.urls import path
from UrlChecker import views


urlpatterns = [
    path('v1/url', views.v1_valid_url),
]