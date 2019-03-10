from usocketgen.server_handler import Handler
import json

class Logic(Handler):
    def process(self, data):
        order = json.loads(data)
        cmd = order['cmd'] 
        if cmd == None:
            cmd = '_default'
        action = getattr(self, cmd)
        return action(order['args'])

    
    def _formdata(self, msg):
        return bytes([len(msg)]) + bytes(msg, 'utf-8')

    def _default(self, args):
        message = 'no cmd is specified'
        return self._formdata(message)

