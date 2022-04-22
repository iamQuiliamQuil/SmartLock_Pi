from http.server import HTTPServer, BaseHTTPRequestHandler
from ipaddress import ip_address
import ssl
import MyIP
from io import BytesIO
import hardware

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
        output = hardware.handle(body_str).encode()

        response = BytesIO()
        response.write(output)
        #response.write(body)
        self.wfile.write(response.getvalue())

ip_addr = MyIP.get_ip()
httpd = HTTPServer((ip_addr, 8000), SimpleHTTPRequestHandler)
    
print("Server running at:",ip_addr)#prints ip address, we'll want
        #remove this and do something lese eventually
httpd.serve_forever()


#this works but I need it to be encrypted 