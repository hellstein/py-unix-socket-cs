# unix socket client

import socket
import sys
import datetime

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)


# Connect the socket to the port where the server is listening
server_address = './uds_socket'
client_address = './uds_client{!s}'.format(datetime.datetime.now())
sock.bind(client_address)
print('connecting to {}'.format(server_address))
try:
    sock.connect(server_address)
except socket.error as msg:
    print(msg)
    sys.exit(1)


try:
    # Send data
    message = b'This is the message. It will be repeat.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
