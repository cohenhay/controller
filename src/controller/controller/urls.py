
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/core/', include('core.api.urls')),
]

