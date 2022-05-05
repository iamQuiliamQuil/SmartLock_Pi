
import sms

storagePath = "/home/pi/Desktop/SmartLock_Pi/Storage/"

def handle(args):
    arguments = args.split("_", 1)
    command = arguments[0]
    params = ()
    if(len(arguments) > 1):
        params = arguments[1].split("_")
    
    # try the command, throw exeption if failed
    try: return globals()[command](*params)
    except Exception as e: print(repr(e))

def capture(resolution, filetype):
    return"capture"+resolution+filetype

    

def getCapture(filename):
    
    return "corradino.jpg"

def getPictureNames():
    #sends back all png filenames joined by ~'s as one string
    return "~".join(sorted([file for file in listdir("../Storage") if ".png" in file],reverse=True))

def lock():
    
    return "locked"

def unlock():
    
    return "unlocked"