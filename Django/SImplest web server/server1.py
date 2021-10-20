#assume browser exists like chrome and we gonna build web server which connects to browser trhough port 9000
#server is always wakaeup and waits infinitely for incoming requests

#browser/server comunication

from socket import *
def createServer():
    serversocket = socket(AF_INET,SOCK_STREAM) # not a phone call , it's the end point
    try:
        serversocket.bind(('localhost',9000)) #ready to recve call on port 9000
        serversocket.listen(5) #if server is busy it say OS to try for 4 more times
        while(1): # this lopps continues until call get coming and ending. once programmer enter any keys server gets down
            (clientsocket, address) = serversocket.accept()  #ready for accepting call and rest until any request is made
            rd = clientsocket.recv(5000).decode() #server recievs request from browser and decode it
            pieces = rd.split('\n')
            if ( len(pieces) > 0) : print( pieces[0] )

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"

            clientsocket.sendall(data.encode()) #server sends data to browser
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt : #when any key is pressedin IDE server shut downs
        print("\nShutting down...\n") 
    except Exception as exc: #if any unknown error , shown
        print("Error:\n")
        print(exc)
    
    serversocket.close()

print("Access http://localhost:9000") # enter this url in browser
createServer() #calls this function
