import sys, os


class Car:
    def __repr__(self):
        return self.__class__.__name__


class Peugeot(Car):
    def __repr__(self):
        return self.__class__.__name__




# Disable print
def blockPrint():
    sys.stdout = open(os.devnull, 'w')


blockPrint()

print('Hello from models.py module')

# Restore print
def enablePrint():
    sys.stdout = sys.__stdout__

enablePrint()