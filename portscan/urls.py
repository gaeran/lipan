from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views


app_name = 'portscan'


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^(?P<ScanResults_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<pk>[0-9]+)/', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results$', views.ResultsView.as_view(), name='results'),
    #add a new portscan record
    url(r'scan/add/', views.ScanResultsCreate.as_view(), name='scan-create'),
    #delete a record
    url(r'scan/(?P<pk>[0-9]+)/delete/$', views.ScanResultsDelete.as_view(), name='scan-delete'),
    # update a record
    url(r'scan/(?P<pk>[0-9]+)/$', views.ScanResultsUpdate.as_view(), name='scan-update'),
    #add a new app splash page
    url(r'^addapp/$',TemplateView.as_view(template_name='portscan/addapp.html'), name='addapp'),
]
