import json
class API:
    def __init__(self, cli):
        self.cli = cli

    def setCommunication(self, sock):
        self.sock = sock

    def run(self):
        order = self.cli.parse()
        cmd = json.dumps(order).encode()
        message = bytes([len(cmd)]) + cmd
        print('sending {!r}'.format(message))
        self.sock.sendall(message)
        datalen = int.from_bytes(self.sock.recv(1), byteorder='big')
        data = self.sock.recv(datalen)
        print(data)
        print('closing socket')
        self.sock.close()

