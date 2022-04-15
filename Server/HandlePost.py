#from SmartLock_Pi.Hardware_Control import hardware

def handle(request_body):
    if request_body == 'lock':
        
        return b'lock!'
    elif request_body == 'unlock':
        return b'unlock!'
    elif request_body == "picture":
        return b'picture!'
    else: return b'Unrecognized reqest!'
