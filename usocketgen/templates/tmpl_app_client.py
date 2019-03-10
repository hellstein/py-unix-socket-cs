from ui import UI
from usocketgen.client import Client

if __name__ == "__main__":
    server_address = "{{ server_address }}"
    ui = UI()
    c = Client(server_address, ui)
    c.start()

