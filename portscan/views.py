from django.http import Http404
from django.shortcuts import render
from portscan.models import ScanResults
#from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    all_ScanResults = ScanResults.objects.all()
    context = {'all_ScanResults' : all_ScanResults}
    return render(request, 'portscan/index.html', context)

def detail(request, ScanResults_id):
    return HttpResponse("<h2> details for scanresults ID:" + str(ScanResults_id) + "</h2>")
    #    all_ScanResults = ScanResults.objects.all()
    #    context = {'all_ScanResults' : all_ScanResults}
    #try:
    #    ScanResults = ScanResults.objects.get(pk=ScanResults_id)
    #except ScanResults.DoesNotExist:
        #raise Http404("Scan does not exist.")

    #return render(request, 'portscan/detail.html', context)
