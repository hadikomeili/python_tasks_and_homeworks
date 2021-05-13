class student():
    def __init__(self, *args):
        self.args = args

    def printInfo(self):
        print('Maximum =', max(self.args))
        print('Minimum =', min(self.args))
        print('Average=', sum(self.args)/len(self.args))


s1 = student(18, 20, 18, 20)
s1.printInfo()
