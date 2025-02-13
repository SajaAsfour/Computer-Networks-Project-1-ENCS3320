from socket import *
#server port,socket initalization and type
portNum=9966
#creating a TCP socket for incoming request
serverSocket = socket(AF_INET,SOCK_STREAM)
#associate the server port number with this socket
serverSocket.bind(('',portNum))
#the server listen for TCP connection requests from the client with i queued connections
serverSocket.listen(1)
#print a message to tell the client that the server is ready to receive 
print ("The server is ready to receive")
#start getting requests:
while True:
    #when a client sends a TCP connection requests
    connectionSocket, address = serverSocket.accept()
    #create "connectionSocket" dedicated to this client
    sent=connectionSocket.recv(2048).decode()
    print(address)
    IP= address[0]
    port=address[1]
    print("IP: "+ str(IP) +",Port: "+ str(port))
    print("********************************************************")
    print(sent)
    print("********************************************************")
    #if the sentence is not empty, the requested file is gotten from request hrader
    if sent !='':
        request_File=sent.split(' ')[1].replace('/','')
        print("The request File is: "+request_File)
    else:
        #if the request is empty the connection is closed
        connectionSocket.close()
        continue
    #exception in case the request file is not found
    try:
        #if the request is index.html/main.html or any file is found in the project file
        #if the file is not found then exception is raised
        #if the requested file is main.html or index.html
        if request_File == '' or request_File=='main_en.html' or request_File== 'index.html' or request_File =='en':
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: text/html \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            mhtml=open('main_en.html' ,'rb')
            connectionSocket.send(mhtml.read())
            mhtml.close()
        #If the request is /ar then the server response with main_ar.html which is an Arabic version of main_en.html 
        elif  request_File=='ar':
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: text/html \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            mhtml=open('main_ar.html' ,'rb')
            connectionSocket.send(mhtml.read())
            mhtml.close()
        #if the request is an .html file then the server should send the requested html file with Content-Type: text/html.
        elif '.html' in request_File:
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: text/html \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            print('response status: 200 OK\n\n')
            f= open(str(request_File), 'rb')
            connectionSocket.send(f.read())
            f.close()
        #if the request is a .css file then the server should send the requested css file with Content-Type: text/css.
        elif '.css' in request_File:
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: text/css \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            print('response status: 200 OK\n\n')
            f= open(str(request_File), 'rb')
            connectionSocket.send(f.read())
            f.close()
        #if the request is a .png then the server should send the png image with Content-Type: image/png.
        elif '.png' in request_File:
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: image/png \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            print('response status: 200 OK\n\n')
            f= open(str(request_File), 'rb')
            connectionSocket.send(f.read())
            f.close()
        #6-	if the request is a .jpg then the server should send the jpg image with Content-Type: image/jpeg.
        elif '.jpg' in request_File:
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: image/jpeg \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            print('response status: 200 OK\n\n')
            f= open(str(request_File), 'rb')
            connectionSocket.send(f.read())
            f.close()
        #If the request is /cr then redirect to cornell.edu website
        elif request_File =='cr':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            connectionSocket.send("Location: https://www.cornell.edu/\r\n".encode())
        #If the request is /so then redirect to stackoverflow.com website
        elif request_File =='so':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            connectionSocket.send("Location: https://stackoverflow.com/\r\n".encode())
        #If the request is /rt then redirect to ritaj website
        elif request_File =='rt':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            connectionSocket.send("Location: https://ritaj.birzeit.edu/register/\r\n".encode())
        #this is a handler only in order not to get not found error
        elif 'favicon.ico'  ==request_File:
            print()  
        else:
            raise Exception('Not found')
    #if the file is not found in the project
    except Exception as e:
        connectionSocket.send(f"HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send(f"Content-Type: text/html \r\n".encode())
        connectionSocket.send(f"\r\n".encode())
        print(request_File +"test")
        print('\b\bResponse status: 404 Not Found')
        f='<!DOCTYPE html><html>' \
        '<style>*{ text-align: center; }' \
        '#Error{ color: red;}#name{ font-weight: bold;}</style>'\
        '<head>  <title>Error 404</title></head>' \
        '<body>  <div id="Error">   <h1>The file is not found</h1> </div>' \
        '<hr> <div id="name">  <p>Saja Asfour - 1210737</p> <p>Shahd Shreteh - 1210444</p>' \
        '<p>Rouand Bawatneh -1211403</p> </div><hr> <div>' \
        '<p> Ip Adress: '+ str(IP)+ ', Port Number: ' +str(port)+\
        '</p> </div> </body></html>'
        connectionSocket.send(f.encode())
    connectionSocket.close()