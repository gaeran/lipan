#from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from portscan.models import ScanResults, PortResult
from portscan.forms import UserForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth import logout
from django.http import JsonResponse
from django.db.models import Q


class IndexView(generic.ListView):
    template_name = 'portscan/index.html'
    def get_queryset(self):
        return ScanResults.objects.all()


def addapp(request):
    return render(request, 'portscan/addapp.html')

#class DetailView(generic.DetailView):
#    model = ScanResults
#template_name = 'portscan/detail.html'

def detail(request, ScanResults_id):
    scan = get_object_or_404(ScanResults, pk=ScanResults_id)
    return render(request, 'portscan/detail.html', {'scan': scan})

class ResultsView(generic.DetailView):
    model = ScanResults
    template_name = 'portscan/results.html'

class ScanResultsCreate(CreateView):
    model = ScanResults
    fields = ['name', 'ip','firstport', 'lastport']

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                scanlist = ScanResults.objects.filter(user=request.user)
                return render(request, 'portscan/index.html', {'scanlist': scanlist})
    context = {
        "form": form,
    }
    return render(request, 'portscan/register.html', context)
