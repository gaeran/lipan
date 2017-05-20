# Port Scanner script, modified for inclusion in Lipan. Original source
# and relevant copyrights credited to PythonForBeginners:
# http://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python

import subprocess
import sys
import socket

from portscan.models import ScanResults, PortResult
from datetime import datetime

def scan_port(addr, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            result = sock.connect_ex((addr, port))
            return result == 0
        except socket.gaierror:
            print('Hostname could not be resolved. Exiting')
            return False

def scan_range(addr, port1, port2):
    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", addr)
    print("-" * 60)

    response = []
    for p in range(port1, port2):
        response.append((p, scan_port(addr,p)))
    return response
