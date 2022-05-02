import keyboard
import sms

while True:
    try:
        if keyboard.is_pressed('q'):
            #sms.send("15186505491", "hello from the other pi")#quillan's phone #
            print("pressed q")
            break
    
    except:
        print("didn't press q")
        break

# remove the break or it will fail immediately
# no work ):