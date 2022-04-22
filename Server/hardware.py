import RPi.GPIO as GPIO
from time import sleep, strftime, gmtime
from picamera import PiCamera

def handle(args):
    arguments = args.split("_", 1)
    command = arguments[0]
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
    camera.capture("/home/pi/Desktop/SmartLock_Pi/Storage/" + filename, filetype)
    camera.close()
    return "picture taken"

def toggleLock():
    led = 17

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)

    GPIO.output(led, GPIO.HIGH)
    sleep(5)
    GPIO.output(led, GPIO.LOW)
    return "lock changed"