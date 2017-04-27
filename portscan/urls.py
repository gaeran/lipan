from django.conf.urls import url, include
from . import views


app_name = 'portscan'


urlpatterns = [
    #/Portscan/
    url(r'^$', views.index, name='index'),

    #/Portscan/scan ID number
    url(r'^(?P<ScanResults_id>[0-9]+)/$', views.detail, name='detail'),

    #/portscan/scan id/favorite
    url(r'^(?P<ScanResults_id>[0-9]+)/favorite/$', views.favorite, name='favorite')
]
