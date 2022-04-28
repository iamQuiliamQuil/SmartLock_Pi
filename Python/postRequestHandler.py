from inspect import getmembers, isfunction
#Quillan's machine
#import hardwareIMPERSONATOR as hardware
#Pi
import hardware
import UUIDManager as um

#takes body decoded to string as argument 
#returns utf-8 bytes
def handleRequest(request):
    #requests should have a as uuid=UUID,request=FUNCTION-ARGS
    #we make a dictionary out of components of the reqest, 
        # each tuple correspoding to a 'key=value' in request
    requestPieces = request[1:].split("Q")
    requestDict = dict()
    for piece in requestPieces: #TODO: find better variable names omfg
        piecePieces = piece.split("~")
        print(piecePieces)
        requestDict[piecePieces[0]] = piecePieces[1]

    print(requestDict)
    sent_uuid = requestDict['uuid']
    uuidMan = um.UUIDManagerSingleton()
    if not uuidMan.UUIDIsValid(sent_uuid):
        #obviously we should not send them the invalid uuid's but this will be useful for testing for now
        return bytes("UUID invalid. Should be from:"+str(uuidMan.registered_uuids),"utf-8")
    else:
        hardwareFunctions = [member[0] for member in getmembers(hardware, isfunction)]
        request = requestDict["request"]
        #see hardware.handle for an explanation of the line below
        command = request.split("_", 1)[0]
        if command in hardwareFunctions:
            print(request)
            result = hardware.handle(request)
            print(type(result))
            print(type(result) is bytes)
            if type(result) is bytes:
                return result
            return bytes(hardware.handle(request),"utf-8")
        else:
            return bytes(request+" is not a valid request name!", "utf-8")