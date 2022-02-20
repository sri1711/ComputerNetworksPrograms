import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind(('localhost',5000))
addr = ('localhost',5000)

while True:
    msg,fromaddr  = server.recvfrom(1024)
    print("message : ",msg.decode())
    server.sendto(bytes("Recieved MEssage",'utf-8'),addr)



