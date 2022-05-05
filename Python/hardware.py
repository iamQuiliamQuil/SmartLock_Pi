#libraries
from PIL import Image
from time import sleep, strftime, gmtime
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from picamera import PiCamera
from io import BytesIO
from os import listdir
from os import path
from os import remove
from distutils.util import strtobool

#local files
import sms

storagePath = "/home/pi/Desktop/SmartLock_Pi/Storage/Captures/"

flagsPath = "/home/pi/Desktop/SmartLock_Pi/Python/flags.txt"
if not path.isfile(flagsPath):
    with open(flagsPath, "w") as file:
        file.write("locked=False")

def __getFlags():
    flags = {}
    with open(flagsPath) as file:
        flagStrings = file.read().split("\n")
        for flagString in flagStrings:
            flagData = flagString.split("=")
            flags[flagData[0]] = flagData[1]
    return flags

def __dictToStr(dictionary):
    dictStr = ""
    for key, value in dictionary.items():
        dictStr += key + "=" + value + "\n"
    dictStr = dictStr[:-1]
    return dictStr

def __setFlag(flagName, flagValue):
    flags = __getFlags()
    flags[flagName] = str(flagValue)
    with open(flagsPath, "w") as file:
        file.write(__dictToStr(flags))

def __getFlag(flagName):
    flags = __getFlags()
    return bool(strtobool(flags[flagName]))

def __checkFlag(flagName, flagValue):
    return flagValue == __getFlag(flagName)

def handle(args):
    arguments = args.split("_", 1)
    command = arguments[0]
    params = ()
    if(len(arguments) > 1):
        params = arguments[1].split("_")
    
    # try the command, throw exception if failed
    try: return globals()[command](*params)
    except Exception as e: print(repr(e))

def capture(resolution, filetype):
    if resolution == "max":
        resolution = (3280, 2464)
    else:
        resolution = [int(i) for i in resolution.split("x")]
    
    camera = PiCamera()
    camera.resolution = resolution

    sleep(2) # for camera warmup
    # day-month-year-hour-minute-second
    filename = strftime("%d-%m-%y-%H-%M-%S." + filetype, gmtime())
    camera.capture(storagePath + filename, filetype)
    camera.close()
    #sms.send("15186505491", "Image Captured!\n" + filename)
    return filename

def getCapture(filename):
    imgBytes = BytesIO()
    filepath = storagePath + filename
    filetype = path.splitext(filename)[1][1:]
    print(filepath)
    with Image.open(filepath) as img:
        img.save(imgBytes, filetype)
    imgBytes.seek(0) # start of bytes
    return imgBytes.read()

def deleteCapture(filename):
    filepath = storagePath + filename
    remove(filepath)
    return filename + " was deleted"

def getPictureNames():
    #sends back all png filenames joined by ~'s as one string
    return "~".join(sorted(listdir(storagePath), reverse=True))

def lock():
    if __checkFlag("locked", False):
        kit = MotorKit()
        for i in range(100):
            kit.stepper1.onestep(direction=stepper.FORWARD)
        __setFlag("locked", True)
        return "locked"
    return "did not lock"

def unlock():
    if __checkFlag("locked", True):
        kit = MotorKit()
        for i in range(100):
            kit.stepper1.onestep(direction=stepper.BACKWARD)
        __setFlag("locked", False)
        return "unlocked"
    return "did not unlock"

def getState():
    return str(__getFlag("locked"))

#print(getPictureNames())
#print(getCapture("29-04-22-16-15-22.png"))