from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

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
httpd = HTTPServer(('169.226.237.222', 8000), SimpleHTTPRequestHandler)
#httpd = HTTPServer(('169.226.216.111', 8000), SimpleHTTPRequestHandler)
#httpd = HTTPServer(('localhost', 4443), BaseHTTPRequestHandler)

"""httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="key.pem", 
        certfile='cert.pem', server_side=True)"""
        

    

httpd.serve_forever()

#this works but I need it to be encrypted and I need to be able to write
#  custom command I THINK