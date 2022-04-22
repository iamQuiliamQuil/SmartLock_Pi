from PIL import Image
from time import sleep, strftime, gmtime
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from picamera import PiCamera
from io import BytesIO

storagePath = "/home/pi/Desktop/SmartLock_Pi/Storage/"

def handle(args):
    arguments = args.split("_", 1)
    command = arguments[0]
    command = command[1:]
    params = ()
    if(len(arguments) > 1):
        params = arguments[1].split("_")

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
    filename = strftime("%d-%m-%y_%H:%M:%S." + filetype, gmtime())
    camera.capture(storagePath + filename, filetype)
    camera.close()
    return filename

def getCapture(filename):
    imgBytes = BytesIO()
    filepath = storagePath + "/" + filename
    with Image.open(filepath) as img:
        img.save(imgBytes, "png")
    return imgBytes

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

getCaptures()