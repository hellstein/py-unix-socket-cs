# unix socket client

import socket
import sys
import datetime
from .client_api import API


class Client:
    def __init__(self, server_address, cli, client_address=None):
        self.server_address, self.client_address = server_address, client_address
        self.api = API(cli)

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



