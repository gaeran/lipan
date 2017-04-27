from django.db import models

# Create your models here.
class ScanResults(models.Model):
    name = models.CharField(max_length=250, default="scan name")
    ip = models.CharField(max_length=70)
    is_favorite = models.BooleanField(default=False)
    #scanDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' - ' + self.ip


class PortResult(models.Model):
    assignedScanResult = models.ForeignKey(ScanResults, on_delete=models.CASCADE)
    portNumber = models.CharField(max_length=5, default='0')
    state = models.CharField(max_length=20, default='undefined')
    service = models.CharField(max_length=70, default='undefined')
    latency = models.CharField(max_length=5, default='0')
    port_type = models.CharField(max_length=5, default='undefined')

    def __str__(self):
        return self.portNumber + ' - ' + self.state + ' - ' + self.service + ' - ' + self.latency + ' - ' + self.port_type
