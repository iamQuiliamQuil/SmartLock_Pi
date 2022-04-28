import keyboard
while True:
    try:
        if keyboard.is_pressed('q'):
            print("pressed q")
            break
    except:
        print("didn't press q")
        break

# remove the break or it will fail immediately
# no work ):