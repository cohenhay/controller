from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from .views import ServerRudView, ServerAPIView


urlpatterns = [
    url(r'^$', ServerAPIView.as_view(), name='post-listcreate'),
    url(r'^(?P<pk>\d+)/$', ServerRudView.as_view(), name='post-rud')
]   