# unix socket server
import socket
import sys
import os

class Server:
    def __init__(self, address, api):
        self.address, self.api = address, api
        # Make sure the socket does not already exist
        try:
             os.unlink(self.address)
        except OSError:
            if os.path.exists(self.address):
                raise
    
    def start(self):
        # Create a UDS (Unix Domain Socket) socket
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        # Bind the socket to the address
        print('starting up on {}'.format(self.address))
        self.sock.bind(self.address)
        self.sock.listen()
        self.run()

    def run(self):
        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = self.sock.accept()
            t = self.api(connection, client_address)
            t.start() 


if __name__ == "__main__":
    from server_api import API
    from server_handler import Handler
    address = './uds_socket'
    conf = ''
    API.handler = Handler(conf)
    s = Server(address, API)
    s.start()
