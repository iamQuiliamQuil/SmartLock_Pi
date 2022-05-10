# checks button presses
# sometimes the butons press fires twice
# would benefit from a debounce
# A debounce system is a set of code that keeps a function from running too many times.
# definition source: https://developer.roblox.com/en-us/articles/Debounce

import hardware
import sms
import MyIP

from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1" # prevents pygame from printing stuff to console, pointless addition

import RPi.GPIO as GPIO
import pygame

pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Desktop/SmartLock_Pi/Storage/Sounds/doorbell-1.wav") # load the audio into the pygame thing

def doorbell(channel): # for the outside button
    pygame.mixer.music.play() # play the sound
    filename = hardware.capture("max","jpeg") # capture an image
    #myIP might not work
    sms.send_image("19146190386",filename,MyIP.get_ip(),"Someone is at your door!") # send the notification

def toggleLock(channel): # for the inside button
    if hardware.__getFlag("locked") == False:
        hardware.lock()
    elif hardware.__getFlag("locked") == True:
        hardware.unlock()

insideButton = 17 # the GPIO ports
outsideButton = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(insideButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set button as input and use the pull up resistor
GPIO.setup(outsideButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(insideButton, GPIO.RISING, callback=toggleLock) # when a LOW to HIGH is detected, call the appropriate function
GPIO.add_event_detect(outsideButton, GPIO.RISING, callback=doorbell)

input("Press enter to quit\n\n") # creates infinite loop

GPIO.cleanup()
