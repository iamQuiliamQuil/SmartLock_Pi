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
        data = app.recv(size)
        if data:
            print(data)
            client.send(data)
except:
    print("Closing socket")
    client.close()
    s.close()