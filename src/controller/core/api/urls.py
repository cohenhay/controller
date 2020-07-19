from django.conf.urls import url
from .views import ServerRudView, ServerAPIView

app_name ='api-core'
urlpatterns = [
    url(r'^$', ServerAPIView.as_view(), name='post-listcreate'),
    url(r'^(?P<pk>\d+)/$', ServerRudView.as_view(), name='post-rud')
]   