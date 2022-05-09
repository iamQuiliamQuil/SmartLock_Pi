from inspect import getmembers, isfunction
#Quillan's machine
#import hardwareIMPERSONATOR as hardware
#Pi
import hardware
import UUIDManager as um
import PhoneNumberManager as pnm


#takes body decoded to string as argument 
#returns utf-8 bytes
def handleRequest(request):
    #requests should have a as uuid~UUIDQrequest~FUNCTION-ARGS
    #we make a dictionary out of components of the reqest, 
        # each tuple correspoding to a 'key=value' in request
    requestPieces = request[1:].split("Q") #TODO: find better way of accounting for C# requests having extra start symbol thing
    if len(requestPieces) < 2:
        return b"Request does not meet specified format: uuid~UUIDQrequest~FUNCTION-ARGS"
        #TODO: figure out why "=","," characters from app get turned to garbage, change delimiters on app and here
    requestDict = dict()
    for piece in requestPieces: #TODO: find better variable names omfg
        piecePieces = piece.split("~")
        print(piecePieces)
        requestDict[piecePieces[0]] = piecePieces[1]

    print(requestDict)
    try: 
        sent_uuid = requestDict['uuid'] 
    except KeyError: 
        return b"Error: all post requests must be sent with uuid. uuid was not sent or was incorrectly formatted"
    
    uuidMan = um.UUIDManagerSingleton()
    if not uuidMan.UUIDIsValid(sent_uuid):
        #obviously we should not send them the invalid uuid's but this will be useful for testing for now
        return bytes("UUID invalid. Should be from:"+str(uuidMan.registered_uuids),"utf-8")
    else:
        hardwareFunctions = [member[0] for member in getmembers(hardware, isfunction)]
        request = requestDict["request"]
        #see hardware.handle for an explanation of the line below
        try:
            command = request.split("_", 1)[0]
        except KeyError:
            return b"uuid is valid, but no request was sent or request was incorrectly formatted"
        if command in hardwareFunctions:
            print(request)
            result = hardware.handle(request)
            #print(type(result))
            #print(type(result) is bytes)
            if type(result) is bytes:
                return result
            return bytes(result,"utf-8")
        elif command == "addPhone":
            phoneNumMan = pnm.PhoneNumberManagerSingleton()
            result = bytes(phoneNumMan.addNum(request.split("_", 1)[1]),"utf-8")
            print("Our Current Phone Numbers:",phoneNumMan.getNums())
            return result
        elif command == "removePhone":
            result = bytes(phoneNumMan.removeNum(request.split("_", 1)[1]),"utf-8")
            print("Our Current Phone Numbers:",phoneNumMan.getNums())
            return result
        else:
            return bytes(request+" is not a valid request name!", "utf-8")
            #add some stuff for adding phone numbers