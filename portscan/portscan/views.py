#from django.http import Http404
from django.shortcuts import render, get_object_or_404
#from portscan.models import ScanResults, PortResult

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from portscan.models import ScanResults, PortResult
#from django.template import loader
from django.http import HttpResponse

class IndexView(generic.ListView):
    template_name = 'portscan/index.html'
    def get_queryset(self):
        return ScanResults.objects.all()


def addapp(request):
    return render(request, 'portscan/addapp.html')

class DetailView(generic.DetailView):
    model = ScanResults
    template_name = 'portscan/detail.html'

class ScanResultsCreate(CreateView):
    model = ScanResults
    fields = ['name']
