import threading
class API(threading.Thread):
    def __init__(self, connection, client_address):
        super(API, self).__init__()
        self.connection, self.client_address = connection, client_address

    def run(self):
        try:
            print('connection from ', self.client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = self.connection.recv(16)
                print('received {!r}'.format(data))
                if data:
                    print('sending data back to the client')
                else:
                    print('no data from ', self.client_address)
                    break
        finally:
            # Clean up the connection
            self.connection.close()

