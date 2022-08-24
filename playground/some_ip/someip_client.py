import enum
import socket
import sys

sys.path.append("../../protocols")

# Import enum

# Import PDU
from some_ip.transport.ethernet.header import SOMEIPHeader

# Craft a DoIP packet by getting Ethernet transport and craft final message as Scapy

some_ip = SOMEIPHeader()
some_ip.message_id = 0xFFFF0000
some_ip.length = 0x8
some_ip.request_id = 0xDEADBEEF
some_ip.protocol_version = 0x01
some_ip.interface_version = 0x01
some_ip.message_type = 0x01
some_ip.return_code = 0x00

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 30501)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.bind(('', 30491))
sock.connect(server_address)

try:
    # Send crafted DoIP packets
    sock.send(bytes(some_ip))
finally:
    print('closing socket')
    sock.close()