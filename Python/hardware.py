# this performs some task based on the command it recieves

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

# first i create a flags.txt (unless it already exists)
# flags.txt holds data about certain states of the system
# it is currently only being used to check if the lock is locked or unlocked
# it is possible to add more flags
flagsPath = "/home/pi/Desktop/SmartLock_Pi/Python/flags.txt"
if not path.isfile(flagsPath):
    with open(flagsPath, "w") as file:
        file.write("locked=False")

# returns a ditionary for every flag in flags.txt
def __getFlags():
    flags = {}
    with open(flagsPath) as file:
        flagStrings = file.read().split("\n")
        for flagString in flagStrings:
            flagData = flagString.split("=")
            flags[flagData[0]] = flagData[1]
    return flags

# converts a dictonary to a string that can be written to flags.txt
def __dictToStr(dictionary):
    dictStr = ""
    for key, value in dictionary.items():
        dictStr += key + "=" + value + "\n"
    dictStr = dictStr[:-1]
    return dictStr

# sets a flag
def __setFlag(flagName, flagValue):
    flags = __getFlags() # must first get the flags
    flags[flagName] = str(flagValue)
    with open(flagsPath, "w") as file:
        file.write(__dictToStr(flags)) # write it to flags.txt

def __getFlag(flagName):
    flags = __getFlags() # must first get the flags
    return bool(strtobool(flags[flagName])) # return the state of the flag

# performs a comparision and returns a boolean
# tells you if the flag was equal to the value
def __checkFlag(flagName, flagValue):
    return flagValue == __getFlag(flagName)

# takes a command as a parameter
def handle(args):
    arguments = args.split("_", 1) # command format: commandName_parameter1_paremeter2
    command = arguments[0]
    params = ()
    if(len(arguments) > 1): # if there is a parameter
        params = arguments[1].split("_")
    
    # try the command, throw exception if failed
    try: return globals()[command](*params) # calls a function in this script and passes the parameters
    except Exception as e: print(repr(e))

# command examples
# how things should be done by default:
# capture_max_jpeg
# can also specify resolution and filetype
# capture_1920x1080_png
def capture(resolution, filetype):
    if resolution == "max":
        resolution = (3280, 2464)
    else:
        resolution = [int(i) for i in resolution.split("x")]
    
    camera = PiCamera()
    camera.resolution = resolution

    sleep(2) # for camera warmup
    # day-month-year-hour-minute-second
    # should be changed to: year-month-day-hour-minute-second to properly sort images by date
    filename = strftime("%d-%m-%y-%H-%M-%S." + filetype, gmtime())
    camera.capture(storagePath + filename, filetype)
    camera.close()
    # CHANGE THIS PHONE NUMBER
    #sms.send("15186505491", "Image Captured!\n" + filename) # used to send notification
    return filename

# command example
# getCapture_00-00-00-00-00-00.jpeg
def getCapture(filename):
    imgBytes = BytesIO() # for storing the image data
    filepath = storagePath + filename
    filetype = path.splitext(filename)[1][1:]
    print(filepath)
    with Image.open(filepath) as img:
        img.save(imgBytes, filetype) # writes the image data to bytes
    imgBytes.seek(0) # start of bytes
    return imgBytes.read()

# command example
# deleteCapture_00-00-00-00-00-00.jpeg
def deleteCapture(filename):
    filepath = storagePath + filename
    remove(filepath)
    return filename + " was deleted"

# command example
# getPictureNames
def getPictureNames():
    #sends back all png filenames joined by ~'s as one string
    return "~".join(sorted(listdir(storagePath), reverse=True))

# command example
# lock
def lock():
    # check the state to ensure that the lock NEVER move twice in same direction
    if __checkFlag("locked", False):
        kit = MotorKit()
        for i in range(100):
            kit.stepper1.onestep(direction=stepper.FORWARD) # rotate forward 180 degrees
        __setFlag("locked", True)
        return "locked"
    return "did not lock"

# command example
# unlock
def unlock():
    # check the state to ensure that the lock NEVER move twice in same direction
    if __checkFlag("locked", True):
        kit = MotorKit()
        for i in range(100):
            kit.stepper1.onestep(direction=stepper.BACKWARD) # rotate backward 180 degrees
        __setFlag("locked", False)
        return "unlocked"
    return "did not unlock"

# command example
# getState
def getState():
    return str(__getFlag("locked"))
