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
