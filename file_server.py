import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',12000))
server.listen(3)
client,addr = server.accept()

fileName = client.recv(1024).decode()
print('Connection Established...')
file = open(fileName,'wb')

while True:
    msg = client.recv(1024).decode()
    # print(str(msg))
    if str(msg) == 'done':
        break
    file.write(msg.encode())
file.close()
client.shutdown(2)
client.close()
server.close()
print('received')