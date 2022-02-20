
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',12000))

print('\n  *********************Connected to Server *********************')
while True:
    client_msg = input('-->')
    client.send(client_msg.encode())
    if client_msg in ['quit','exit','bye']:
        break
    server_msg = client.recv(1024).decode()
    print('<--`',server_msg)
    

