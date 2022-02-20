import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('localhost',5000))

server.listen(3)
print('Waiting for Connection...')

while True:
    client,addr = server.accept()
    print("Connected to ",addr)
    msg = client.recv(1200).decode()
    print("Message Recieved : ",msg)
    client.send(bytes(msg,'utf-8'))
    print("Message Sent to client")

    