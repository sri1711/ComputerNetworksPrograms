
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',12000))
server.listen(5)
print('\n *********************Connected to Client************************')



client,addr = server.accept()
while True:
    client_msg = client.recv(1024).decode()
    print('<--',client_msg)
    
    if('bye' == client_msg):
        server_msg = 'Bye, see you later'
        client.send(server_msg.encode())
        break

    server_msg = input('-->')
    client.send(server_msg.encode())