import os
class Writer:
    """
    Write parser result into python file
    """
    def __init__(self, directory):
        self.directory = directory
        os.mkdir(self.directory)

    def create(self, content):
        for fname, code in content.items():
            with open(os.path.join(self.directory, fname), 'w') as f:
                f.write(code)

