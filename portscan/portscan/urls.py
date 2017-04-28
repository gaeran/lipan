from django.conf.urls import url, include
from . import views


app_name = 'portscan'


urlpatterns = [
    #/Portscan/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/Portscan/scan ID number
    url(r'^(?P<pk>[0-9]+)/', views.DetailView.as_view(), name='detail'),
    url(r'scan/add/', views.ScanResultsCreate.as_view(), name='scan-create')
    url(r'addapp/', views.addapp, name='addapp'),
]
