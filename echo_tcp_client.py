import socket

client  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket Created')
client.connect(('localhost',5000))
msg = input('Enter Message: ')

client.send(bytes(msg,'utf-8'))

print("Message Recieved : ",client.recv(1024).decode('utf-8'))
