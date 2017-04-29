from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views


app_name = 'portscan'


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^(?P<ScanResults_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/results$', views.ResultsView.as_view(), name='results'),
    url(r'scan/add/', views.ScanResultsCreate.as_view(), name='scan-create'),
    url(r'^addapp/$',TemplateView.as_view(template_name='portscan/addapp.html'), name='addapp'),
    
]
