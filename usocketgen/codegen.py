import json
from jinja2 import Environment, Template, FileSystemLoader

class CodeGener:
    """
    Init templates 
    """
    def __init__(self, info):
        self.info = info
        env = Environment(
            loader=FileSystemLoader(searchpath='./templates')
        )

        self.tmpl = {}
        #self.tmpl['concreatestate'] = env.get_template('state_tmpl.py')

        self.codeinfo = {}

    def genCode(self):
        return self.codeinfo

