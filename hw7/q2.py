class Indenter:
    """a class for print indent in a text"""
    cnt = -1
    indent = '\t'

    def __init__(self):
        # self.text = text
        self.cnt = -1
        self.indent = ''

    def print(self, text: str):
        assert isinstance(text, str), 'invalid input!!!'
        for i in range(self.cnt):
            self.indent+= '\t'
        res = self.indent + text
        print(res)

    def __enter__(self):
        self.cnt += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.indent = ''
        self.cnt = -1
        return True


#============================== test case
with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('talk is cheap')
        with indent:
            indent.print('show me the code ')
    indent.print('Torvalds')

