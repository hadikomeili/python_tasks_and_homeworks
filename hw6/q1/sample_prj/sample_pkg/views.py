from .models import Car, Peugeot
import sys, os






class CarView:
    model = Car

    def show(self):
        print(self.model())



class PeugeotView:
    model = Peugeot

    def show(self):
        print(self.model())



# Disable print
def blockPrint():
    sys.stdout = open(os.devnull, 'w')


blockPrint()

print('Hello from views.py module')


# Restore print
def enablePrint():
    sys.stdout = sys.__stdout__


enablePrint()
