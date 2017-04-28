from django.contrib import admin
from .models import ScanResults, PortResult
# Register your models here.
admin.site.register(ScanResults)
admin.site.register(PortResult)
