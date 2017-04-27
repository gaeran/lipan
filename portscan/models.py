from django.db import models

# Create your models here.
class ScanResults(models.Model):
    name = models.CharField(max_length=250, default="scan name")
    ip = models.CharField(max_length=70)
    #scanDate = models.DateTimeField(auto_now_add=True)


class PortResult(models.Model):
    assignedScanResult = models.ForeignKey(ScanResults, on_delete=models.CASCADE)
    portNumber = models.IntegerField
    state = models.CharField(max_length=20)
    service = models.CharField(max_length=70)
    latency = models.IntegerField
    port_type = models.CharField(max_length=5)
