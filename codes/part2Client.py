import socket

message = input("Enter Valid ID")
serverName = socket.gethostbyname(socket.gethostname())

# Set up the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((serverName, 9955))

# Send the student ID to the server
client_socket.send(message.encode())

# Receive the response from the server
response = client_socket.recv(1024).decode()
# Close the connection
client_socket.close()