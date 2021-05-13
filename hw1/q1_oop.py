class tabel():
    def __init__(self, number):
        self.number: int = number

    def printTabel(self):
        for i in range(1, self.number + 1):
            for j in range(1, self.number + 1):
                print(i * j, end= '\t')
            print()

t1 = tabel(int(input('enter number?\n')))
t1.printTabel()