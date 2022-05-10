# this is the python implementation of bluetooth
# this most likely can work but wasn't tested
# would theoretically run on the app
import bluetooth

piAddress = "E4:5F:01:92:40:3F" # the pi's mac address
port = 22
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((piAddress, port))
while 1:
    text = input()
    if text == "quit":
        break
    s.send(bytes(text, "UTF-8")) # send the message inputted to the console as bytes
s.close()
