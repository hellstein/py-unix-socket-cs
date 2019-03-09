# unix socket server

import socket
import sys
import os
import threading

server_address = './uds_socket'


# Make sure the socket does not already exist

try:
     os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# Create a UDS (Unix Domain Socket) socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Bind the socket to the address
print('starting up on {}'.format(server_address))

sock.bind(server_address)

sock.listen()


def worker(connection, client_address):
    try:
        print('connection from ', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
            else:
                print('no data from ', client_address)
                break
    finally:
        # Clean up the connection
        connection.close()


while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    t = threading.Thread(target=worker, args=(connection, client_address,))
    t.start() 
    print(threading.activeCount())
