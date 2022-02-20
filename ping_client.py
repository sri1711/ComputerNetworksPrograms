from ast import While
import socket

client  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

addr = ('',12000)

while True:
    msg = input("Enter :")
    
