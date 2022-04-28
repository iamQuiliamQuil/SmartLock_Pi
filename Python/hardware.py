from PIL import Image
from time import sleep, strftime, gmtime
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from picamera import PiCamera
from io import BytesIO
from os import listdir
from os.path import join

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
    return filename

def getCapture(filename):
    imgBytes = BytesIO()
    filepath = storagePath + filename
    print(filepath)
    with Image.open(filepath) as img:
        img.save(imgBytes, "png")
    imgBytes.seek(0) # start of bytes
    return imgBytes.read()

def getPictureNames():
    #sends back all png filenames joined by ~'s as one string
    return "~".join(sorted([file for file in listdir("../Storage") if ".png" in file],reverse=True))

def lock():
    kit = MotorKit()
    for i in range(100):
        kit.stepper1.onestep(direction=stepper.FORWARD)
    return "locked"

def unlock():
    kit = MotorKit()
    for i in range(100):
        kit.stepper1.onestep(direction=stepper.BACKWARD)
    return "unlocked"