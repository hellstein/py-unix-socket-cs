# unix socket client

import socket
import sys
import datetime



class Client:
    def __init__(self, server_address, api, client_address=None):
        self.server_address, self.client_address = server_address, client_address
        self.api = api

    def start(self):
        # Create a UDS socket
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        if self.client_address != None:
            self.sock.bind(self.client_address)
        print('connecting to {}'.format(self.server_address))
        try:
            self.sock.connect(self.server_address)
        except socket.error as msg:
            print(msg)
            sys.exit(1)
        self.run()

    def run(self):
        self.api.setCommunication(self.sock)
        self.api.run()


if __name__ == "__main__":
    from client_api import API
    from client_cli import CLI
    server_address = 'uds_socket'
    conf = ''
    cli = CLI(conf)
    api = API(cli)
    c = Client(server_address, api)
    c.start()

