import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',12000))
fileName = "HelloNew.txt"
client.send(fileName.encode())
file = open('Hello.txt','r')

while True:
    bytes = file.read(1024)
    print(bytes)
    if not bytes:
        break
    client.send(bytes.encode())

done ='done'
client.send(done.encode())
print('File Sent')
client.close()
    
