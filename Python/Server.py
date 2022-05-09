from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
from io import BytesIO
import sys

import UUIDManager as um
import MyIP
import postRequestHandler
import sms
import PhoneNumberManager as pnm
sys.path.insert(1, '../Storage')
import PictureServer
#import hardware  

#ip_addr

#PEM pass phrase: password
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

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

#if we want to keep this line at all, we should use phone num manager for it
phone_num_man = pnm.PhoneNumberManagerSingleton()
phone_num_man.addNum("15186505491") #Quillan's hpone
phone_num_man.addNum("19186190386") #Ender's phone

phone_nums = phone_num_man.getNums()
for num in phone_nums:
    sms.send(num,"Server running at: "+ip_addr+":8000")
    sms.send_image("15186505491","29-04-22-16-15-22.png",ip_addr,"hey")
#sms.send("15186505491","server running at: "+ip_addr+":8000")
print("Main Server running at:",ip_addr) #prints ip address, and that is just fine. Why remove it?

PictureServer.launch(ip_addr) #server for hosting images need to be launched as well
httpd.serve_forever()


#this works but I need it to be encrypted 