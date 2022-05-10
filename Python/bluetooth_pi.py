# this is the python implementation of bluetooth
# this most likely can work but wasn't tested
# would theoretically run on the pi

import bluetooth

piAddress = "E4:5F:01:92:40:3F"
port = 22
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((piAddress, port))
s.listen(backlog)
try:
    app, address = s.accept()
    while 1:
        data = app.recv(size) # recieve some stuff
        if data:
            print(data) # print what it got
            client.send(data) # send it back for verification on the app side of things
except:
    print("Closing socket")
    client.close()
    s.close()
