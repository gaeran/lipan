#Port Scanner script, modified for inclusion in Lipan. Original source and relevant copyrights credited to PythonForBeginners: http://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python

import subprocess
import sys
from portscan.models import ScanResults, PortResult
from datetime import datetime
import web



remoteServer = ScanResults.ip
remoteServerIP = socket.gethostbyname(remoteServer)
port1 = ScanResults.firstport
port2 = ScanResults.lastport
t1 = datetime.now()

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

try:
    for port in range(port1, port2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            #this creates a new row in portResult which established a given port number and its status as OPEN
        sock.close()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
