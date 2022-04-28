import bluetooth

piAddress = "E4:5F:01:92:40:3F"
port = 22
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((piAddress, port))
while 1:
    text = input()
    if text == "quit":
        break
    s.send(bytes(text, "UTF-8"))
s.close()