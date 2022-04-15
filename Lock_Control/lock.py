import RPi.GPIO as GPIO
from time import sleep

def on():
    #I have no idea what I'm doing with this led stuff this might all be garbage
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led,GPIO.OUT)

    GPIO.output(led,GPIO.HIGH)

def off():
    GPIO.output(led,GPIO.LOW)

if __name__ == '__main__':
    led = 17

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led,GPIO.OUT)

    GPIO.output(led,GPIO.HIGH)
    sleep(1)
    GPIO.output(led,GPIO.LOW)