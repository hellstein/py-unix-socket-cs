from unixsocketcs.server_handler import Handler
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


    def start(self, args):
        message = "result of start"
        return self._formdata(message)

    def stop(self, args):
        message = "result of stop"
        return self._formdata(message)

    def install(self, args):
        message = "result of install"
        return self._formdata(message)

    def uninstall(self, args):
        message = "result of uninstall"
        return self._formdata(message)

    def version(self, args):
        message = "result of version"
        return self._formdata(message)

    def status(self, args):
        message = "result of status"
        return self._formdata(message)


