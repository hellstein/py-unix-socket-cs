from usocketgen.client_cli import CLI

class UI(CLI):
    def __init__(self, prog="{{ client_prog_name }}"):
        super(UI, self).__init__(prog)
        subparser = self.parser.add_subparsers(title='commands', dest='cmd', help='commands help')

