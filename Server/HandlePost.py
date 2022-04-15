from SmartLock_Pi.Lock_Control import lock

def handle(request_body):
    if request_body == 'lock':
        lock
        return b'lock!'
    elif request_body == 'unlock':
        return b'unlock!'
    elif request_body == "picture":
        return b'picture!'
    else: return b'Unrecognized reqest!'
