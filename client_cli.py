import argparse


class CLI:
    def __init__(self, conf):
        parser = argparse.ArgumentParser(description='XXX Client.')
        subparser = parser.add_subparsers(title='commands', dest='cmd', help='commands help')

        parser_4_start = subparser.add_parser('start') 
        parser_4_stop = subparser.add_parser('stop')
        
        self.parser = parser

    def parse(self):
        args = self.parser.parse_args()
        return args
