from django.http import Http404
from django.shortcuts import render, get_object_or_404
from portscan.models import ScanResults, PortResult

from django.views import generic
from portscan.models import ScanResults, PortResult
#from django.template import loader
#from django.http import HttpResponse

















def index(request):
    all_ScanResults = ScanResults.objects.all()
    context = {'all_ScanResults' : all_ScanResults}
    return render(request, 'portscan/index.html', context)


def detail (request, ScanResults_id):
    scanlist = get_object_or_404(ScanResults, pk=ScanResults_id)
    return render(request, 'portscan/detail.html', {'scanlist': scanlist})
