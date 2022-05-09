import RPi.GPIO as GPIO

def pressed(channel):
    print("i've been triggered")

button = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(button, GPIO.RISING, callback=pressed)

input("Press enter to quit\n\n")

GPIO.cleanup()