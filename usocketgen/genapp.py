import argparse
from .confparser import Parser
from .codegen import CodeGener
from .appwriter import Writer

class CLI:
    def __init__(self, prog="Demo program"):
        parser = argparse.ArgumentParser(description=prog)
        parser.add_argument('--conf', dest='conf')
        parser.add_argument('--app', dest='app')
        self.parser = parser

    def parse(self):
        args = vars(self.parser.parse_args())
        return args

if __name__ == "__main__":
    args = CLI().parse()
    cfg, dst = args["conf"], args["app"]
    info = Parser(cfg).info
    codeinfo = CodeGener(info).genCode()
    Writer(dst).create(codeinfo)

