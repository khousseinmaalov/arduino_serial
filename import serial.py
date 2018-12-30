import serial
import threading
import socket

ser = serial.Serial("/dev/ttyACM1",timeout=1)
print(ser)

socket = socket.socket()
socket.bind(('', 15555))

def serv():
	while True:
		debianeuf = client.recv(255)
		ser.write(debianeuf)


	client.close()
	stock.close()

while 1:
	socket.listen(5)
	client, address = socket.accept()
	print("{} connected".format( address ))
	threading.Thread(target=serv).start()
