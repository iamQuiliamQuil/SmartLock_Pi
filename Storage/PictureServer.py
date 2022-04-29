import sys
import os
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../Python')
import MyIP
import postRequestHandler 

def __run_server(ip_addr): #private function
    subprocess.check_call(["./launch.sh", "8001", ip_addr])

def launch(ip_addr):
    n = os.fork()
    # n greater than 0  means parent process
    if n > 0:
        print("Picture Server running at "+ip_addr+":8001")
    # n equals to 0 means child process
    else:
        __run_server(ip_addr)

print(launch(MyIP.get_ip()))

