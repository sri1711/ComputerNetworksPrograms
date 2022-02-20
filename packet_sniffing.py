from asyncio import protocols
import socket
from ssl import get_protocol_name
import struct
import binascii
import textwrap

def main():
    host = socket.gethostbyname(socket.gethostname())
    print("IP ",host)

    conn = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
    conn.bind((host,8080))

    conn.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    conn.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

    while True:
        raw_data,addr = conn.recvfrom(4096)
        dest_mac,src_mat,eth_proto,data = ethernet_frame(raw_data)

def ethernet_frame(data):
    dest_mac,src_mac,proto = struct.unpack('!6s6s2s',data[:14])
    return get_mac_addr(dest_mac),get_mac_addr(src_mac),get_protocol(proto),data[14:]

def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format,bytes_addr)
    mac_address = ':'.join(bytes_str).upper()
    return mac_address

def get_protocol(bytes_proto):
    bytes_str = map('{:02x}'.format,bytes_proto)
    protocol = ''.join(bytes_str).upper()
    return protocol

main()