import socket

target_host = "www.google.com"
target_port = 80

#creating a socket object
client = socket.socket(socket.AF_INET, socket.Sock_STREAM)

#connecting to the client
client.connect((target_host,target_port))

#sending some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#recieve some data
response = client.recv(4096)

print(response.decode())
client.close()
