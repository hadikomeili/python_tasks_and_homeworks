class A(object):
    def __init__(self, a):
        self.a=a
    def method(self):
        print('A method')
class B(object):
    def __init__(self, b1, b2):
        self.b1=b1
        self.b2=b2
    def method(self):
        print('B method')
class C(A, B):
    def __init__(self, name, **kwargs):
        if name=='A':
            A.__init__(self, a=kwargs['a'])
        elif name=='B':
            B.__init__(self, b1=kwargs['b1'], b2=kwargs['b2'])

c=C(name='B', b1=2, b2=3)
c.method()
print(C.mro())