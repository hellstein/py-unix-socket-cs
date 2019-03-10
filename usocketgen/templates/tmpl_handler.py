from usocketgen.server_handler import Handler
import json

class Logic(Handler):
    def process(self, data):
        order = json.loads(data)
        action = getattr(self, order['cmd'])
        return action(order['args'])

