class API:
    def __init__(self, sock):
        self.sock = sock

    def run(self):
        try:
            # Send data
            message = b'This is the message. It will be repeat.'
            print('sending {!r}'.format(message))
            self.sock.sendall(message)

            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                print('received {!r}'.format(data))
        finally:
            print('closing socket')
            self.sock.close()

