#simplest web client which talks to server
# client/server communication

#run the server first in another IDE and then run this in another IDE 
#talks http

import socket 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 9000)) #127.0.0.1 is loop back to same host as we are talking to our own server in same computer
cmd = 'GET http://127.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data)<1:
        break
    print (data.decode(), end= '')

mysock.close()

