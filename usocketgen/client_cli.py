import argparse


class CLI:
    def __init__(self, prog="Demo program"):
        parser = argparse.ArgumentParser(description=prog)
        self.parser = parser

    def parse(self):
        args = self.parser.parse_args()
        return args
