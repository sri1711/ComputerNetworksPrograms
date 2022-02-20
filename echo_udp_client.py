import socket
import sys
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = ('localhost',5000)

print('Connection Ready....')



while True:
    msg = sys.stdin.readline()
    if not msg:
        break
    client.sendto(msg.encode(),addr)
    print('Msg send to server')
    print('****Reply From Server**** : ',client.recvfrom(1024))


