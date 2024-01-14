import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the address given on the command line
server_name = 'localhost'
server_address = (server_name, 5555)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

print('waiting for a connection')
connection, client_address = sock.accept()
print('client connected:', client_address)

while True:
    data = connection.recv(1024)
    print(f'received {data}')
    if not data:
        break

connection.shutdown(socket.SHUT_RDWR)
connection.close()