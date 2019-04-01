from unixsocketcs.client_cli import CLI

class UI(CLI):
    def __init__(self, prog="uds client"):
        super(UI, self).__init__(prog)
        subparser = self.parser.add_subparsers(title='commands', dest='cmd', help='commands help')


        parser_4_start = subparser.add_parser("start") 
        parser_4_stop = subparser.add_parser("stop") 
        parser_4_install = subparser.add_parser("install") 
        parser_4_uninstall = subparser.add_parser("uninstall") 
        parser_4_version = subparser.add_parser("version") 
        parser_4_status = subparser.add_parser("status") 

