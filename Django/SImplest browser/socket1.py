#simplest web browser
#let us talk to socket

import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #makes a phone call
mysock.connect(("data.pr4e.org",80)) # connect to server(call) through port 80
cmd= "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd) #send request 
while True:
    data = mysock.recv(512) #recv data from server
    if len(data) < 1:
        break
    print(data.decode(), end = "")

mysock.close()
