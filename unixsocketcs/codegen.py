import json
from jinja2 import Environment, Template, FileSystemLoader
import os

class CodeGener:
    """
    Init templates 
    """
    def __init__(self, info):
        self.info = info
        tmpldir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
        env = Environment(
            loader=FileSystemLoader(searchpath=tmpldir)
        )

        self.tmpl = {}
        self.tmpl['app_client'] = env.get_template('tmpl_app_client.py')
        self.tmpl['app_server'] = env.get_template('tmpl_app_server.py')
        self.tmpl['handler'] = env.get_template('tmpl_handler.py')
        self.tmpl['handler_fn'] = env.get_template('tmpl_handler_fn.py')
        self.tmpl['ui'] = env.get_template('tmpl_ui.py')
        self.tmpl['ui_subparser'] = env.get_template('tmpl_ui_subparser.py')

        self.codeinfo = {}


    def gen_app_client(self):
        code = self.tmpl['app_client'].render(server_address=self.info['server_address']) + '\n'
        self.codeinfo['app_client.py'] = code

    def gen_app_server(self):
        code = self.tmpl['app_server'].render(server_address=self.info['server_address']) + '\n'
        self.codeinfo['app_server.py'] = code

    def _gen_ui_subparser(self):
        subparser_code = '\n'.join([self.tmpl['ui_subparser'].render(cmd=cmd) for cmd in self.info['features']]) + '\n'
        return subparser_code

    def gen_ui(self):
        ui_code = self.tmpl['ui'].render(client_prog_name=self.info['client_prog_name']) + '\n'
        subparser_code = self._gen_ui_subparser()
        code = '\n'.join([ui_code, subparser_code]) + '\n' 
        self.codeinfo['ui.py'] = code

    def _gen_handler_fn(self):
        handler_fn_code = '\n'.join([self.tmpl['handler_fn'].render(action=cmd) for cmd in self.info['features']]) + '\n'
        return handler_fn_code 

    def gen_handler(self):
        handler_code = self.tmpl['handler'].render() + '\n'
        handler_fn_code = self._gen_handler_fn()
        code = '\n'.join([handler_code, handler_fn_code]) + '\n' 
        self.codeinfo['handler.py'] = code


    def genCode(self):
        self.gen_app_client()
        self.gen_app_server()
        self.gen_ui()
        self.gen_handler()
        return self.codeinfo

