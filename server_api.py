import threading
class API(threading.Thread):
    handler = None 
    def __init__(self, connection, client_address):
        super(API, self).__init__()
        self.connection, self.client_address = connection, client_address

    def run(self):
        try:
            print('connection from ', self.client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                datalen = int.from_bytes(self.connection.recv(1), byteorder='big')
                data = self.connection.recv(datalen)
                print('received {!r}'.format(data))
                if data:
                    print('sending data back to the client')
                    result = self.handler.process(data)
                    self.connection.sendall(result)
                else:
                    print('no data from ', self.client_address)
                    break
        finally:
            # Clean up the connection
            print("close client connection.")
            self.connection.close()

