import sys
import os
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler

# We launch a python server from the command line from a python program. This is so stupid. 
# I was under a lot of pressure. Sorry.

def __run_server(ip_addr): 
    #needs to be run in the same directory as the ./launch.sh, which is what this line is for
    os.chdir('/home/pi/Desktop/SmartLock_Pi/Storage')
    subprocess.check_call(["./launch.sh", "8001", ip_addr])

def launch(ip_addr):
    n = os.fork()
    # n greater than 0  means parent process
    if n > 0:
        print("Picture Server running at "+ip_addr+":8001")
    # n equals to 0 means child process
    else:
        __run_server(ip_addr)


