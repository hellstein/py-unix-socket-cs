from server_api import API
from server_handler import Handler
from server import Server

if __name__ == "__main__":
    address = './uds_socket'
    conf = ''
    API.handler = Handler(conf)
    s = Server(address, API)
    s.start()
