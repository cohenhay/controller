
from django.conf.urls import url, include
from django.urls import path,include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from core.views import HomeView

app_name ='api-core'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', HomeView.as_view()),
    url(r'^api/auth/login/$', obtain_jwt_token, name='api-login'),
    url(r'^api/core/', include('core.api.urls',namespace= 'api-core')),
]