from http.server import HTTPServer, BaseHTTPRequestHandler
from ipaddress import ip_address
import ssl
import MyIP

from io import BytesIO
import HandlePost

#PEM pass phrase: password

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, you have reached SmartLock!\n')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()

        #My code, where all errors lie (probably)
        body_str = body.decode("utf-8")
        print(body_str)
        output = HandlePost.handle(body_str)
    
        response = BytesIO()
        response.write(output)
        #response.write(body)
        self.wfile.write(response.getvalue())

#get ip address with code?
ip_addr = MyIP.get_ip()
#print(ip_addr)

httpd = HTTPServer((ip_addr, 8000), SimpleHTTPRequestHandler)
    

httpd.serve_forever()

#this works but I need it to be encrypted and I need to be able to write
#  custom command I THINK