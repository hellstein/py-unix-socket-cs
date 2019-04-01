from ui import UI
from unixsocketcs.client import Client

if __name__ == "__main__":
    server_address = "./uds_server"
    ui = UI()
    c = Client(server_address, ui)
    c.start()

