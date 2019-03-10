from usocketgen.server_handler import Handler
import json

class Logic(Handler):
    def process(self, data):
        order = json.loads(data)
        print(order['cmd'])
        return b'8whataday'
