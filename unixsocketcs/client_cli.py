import argparse


class CLI:
    def __init__(self, prog="Demo program"):
        parser = argparse.ArgumentParser(description=prog)
        self.parser = parser

    def parse(self):
        r = vars(self.parser.parse_args())
        cmd = r['cmd']
        del r['cmd']
        order = {'cmd': cmd, 'args': r}
        return order
