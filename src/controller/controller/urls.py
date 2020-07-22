
from django.conf.urls import url, include
from django.urls import path,include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static
from core import views


app_name ='api-core'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', views.search, name='search'),
    url(r'', views.upload, name='upload'),
    url(r'^api/auth/login/$', obtain_jwt_token, name='api-login'),
    url(r'^api/core/', include('core.api.urls',namespace='api-core')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



