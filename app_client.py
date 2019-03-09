from client_api import API
from client_cli import CLI
from client import Client

if __name__ == "__main__":
    server_address = 'uds_socket'
    conf = ''
    cli = CLI(conf)
    api = API(cli)
    c = Client(server_address, api)
    c.start()

