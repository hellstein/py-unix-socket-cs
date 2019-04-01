import json
from jinja2 import Environment, Template, FileSystemLoader

class Parser:
    """
    parse conf 
    """
    def __init__(self, conf):
        self.conf, self.info = conf, {}
        self.parse()

    def parse(self):
        with open(self.conf, 'r') as f:
            self.info = json.load(f)
            if 'server_address' not in self.info.keys() or self.info['server_address'] == '':
                self.info['server_address'] = './uds_server'
            if 'client_prog_name' not in self.info.keys() or self.info['client_prog_name'] == '':
                self.info['client_prog_name'] = 'uds client'
            if 'features' not in self.info.keys() or not isinstance(self.info['features'], list):
                self.info['features'] = []
