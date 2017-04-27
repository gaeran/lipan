from django.conf.urls import url, include
from . import views
urlpatterns = [
    #/Portscan/
    url(r'^$', views.index, name='index'),

    #/Portscan/scan ID number
    url(r'^(?P<ScanResults_id>[0-9]+)/$', views.detail, name='detail'),
]
