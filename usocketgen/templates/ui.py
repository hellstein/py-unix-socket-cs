from usocketgen.client_cli import CLI

class UI(CLI):
    def __init__(self, prog="Demo program"):
        super(UI, self).__init__(prog)
        subparser = self.parser.add_subparsers(title='commands', dest='cmd', help='commands help')
        parser_4_start = subparser.add_parser('update') 
        parser_4_stop = subparser.add_parser('remove')

