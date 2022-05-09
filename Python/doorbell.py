import hardware
import sms
import MyIP

from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import RPi.GPIO as GPIO
import pygame

pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Desktop/SmartLock_Pi/Storage/Sounds/doorbell-1.wav")

def doorbell(channel):
    pygame.mixer.music.play()
    filename = hardware.capture("max","jpeg")
    #myIP might not work
    sms.send_image("19146190386",filename,MyIP.get_ip(),"Someone is at your door!")

def toggleLock(channel):
    if hardware.__getFlag("locked") == False:
        hardware.lock()
    elif hardware.__getFlag("locked") == True:
        hardware.unlock()

insideButton = 17
outsideButton = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(insideButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(outsideButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(insideButton, GPIO.RISING, callback=toggleLock)
GPIO.add_event_detect(outsideButton, GPIO.RISING, callback=doorbell)

input("Press enter to quit\n\n")

GPIO.cleanup()