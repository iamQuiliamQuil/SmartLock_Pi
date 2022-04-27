from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
from io import BytesIO

import UUIDManager as um
import MyIP
import postRequestHandler 
#import hardware  

#PEM pass phrase: password
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        #<my code>
        uuidMan = um.UUIDManagerSingleton()
        new_uuid = uuidMan.generateUUID()

        self.wfile.write(bytes(new_uuid,"utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()

        #My code, where all errors lie (probably)
        body_str = body.decode("utf-8")
        print(body_str)

        output = postRequestHandler.handleRequest(body_str)

        response = BytesIO()
        response.write(output)
        #response.write(body)
        self.wfile.write(response.getvalue())

ip_addr = MyIP.get_ip()
#need to change port later
httpd = HTTPServer((ip_addr, 8000), SimpleHTTPRequestHandler)
#context = ssl.SSLContext(ssl.SSLContext.set_default_verify_paths())

httpd.socket = ssl.wrap_socket (httpd.socket, 
    keyfile="key.pem", 
    certfile='cert.pem', server_side=True)
    
print("Server running at:",ip_addr) #prints ip address, we'll want
        #remove this and do something lese eventually
httpd.serve_forever()


#this works but I need it to be encrypted 