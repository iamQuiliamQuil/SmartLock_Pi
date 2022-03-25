import RPi.GPIO as GPIO
from time import sleep

led = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)

GPIO.output(led,GPIO.HIGH)
sleep(1)
GPIO.output(led,GPIO.LOW)