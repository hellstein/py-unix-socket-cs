from ui import UI
from usocketgen.client import Client

if __name__ == "__main__":
    server_address = './uds_socket'
    ui = UI()
    c = Client(server_address, ui)
    c.start()

