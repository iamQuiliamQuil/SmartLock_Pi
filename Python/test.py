"""result = "h".encode()
print(result)
print(type(result))
print(type(result) is bytes)"""
import UUIDManager as um
import hardware
import postRequestHandler as prh
import sms
import MyIP
#print(hardware.getPictureNames())
#hardware.capture("100x100","png")

"""uuids = um.UUIDManagerSingleton()
uuid = uuids.generateUUID()

request = "uuuid~"+uuid+"Qrequest~lock"
print("helooooo")

prh.handleRequest(request)"""

import sys
sys.path.insert(1, '../Storage')
import PictureServer

ip_addr = MyIP.get_ip()
#sms.send("15186505491","heyy")
PictureServer.launch(ip_addr)
sms.send_image("15186505491","29-04-22-16-15-22.png",ip_addr,"hey")

