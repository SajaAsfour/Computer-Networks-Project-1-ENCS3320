import socket
import time
import ctypes
serverPort = 9955
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
def lock_screen():
    try:
        # Set the SPI_SETSCREENSAVEACTIVE parameter to disable the screensaver
        ctypes.windll.user32.SystemParametersInfoW(0x71, 0, 0, 0)

        # Lock the workstation
        ctypes.windll.user32.LockWorkStation()
        print("Screen locked successfully")
    except Exception as e:
        print(f"Error locking screen: {e}")

def client(client_socket, data):
    ids = ["1210737", "1210444", "1211403"]
    if data in ids:
        print("It's valid student ID which is",data)

        # Display message on the server side
        print("The OS will lock screen after 10 seconds...")

        # Send a message to the client
        client_socket.send("Server will lock screen after 10 seconds".encode())

        # Wait for 10 seconds
        time.sleep(10)

        # Call the function to lock the screen
        lock_screen()
    else:
        print("Error: Invalid student ID ")
while True:
    client_socket, addr = serverSocket.accept()
    print("Accepted connection from", addr)

    data = client_socket.recv(1024).decode()
    client(client_socket, data)

    client_socket.close()

