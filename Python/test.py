"""result = "h".encode()
print(result)
print(type(result))
print(type(result) is bytes)"""
import UUIDManager as um
import hardware
import postRequestHandler as prh
#print(hardware.getPictureNames())
#hardware.capture("100x100","png")

uuids = um.UUIDManagerSingleton()
uuid = uuids.generateUUID()

request = "uuuid~"+uuid+"Qrequest~lock"
print("helooooo")

prh.handleRequest(request)