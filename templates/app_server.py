from handler import Logic
from usocketgen.server import Server

if __name__ == "__main__":
    address = './uds_socket'
    logic = Logic() 
    s = Server(address, logic)
    s.start()
