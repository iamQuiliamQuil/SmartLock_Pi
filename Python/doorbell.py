import hardware
import sms
import MyIP

def press():
    filename = hardware.capture("300x300","png")
    #myIP might not work
    sms.send_image("19146190386",filename,MyIP.get_ip(),"Someone is at your door!")

press()