class A:
    def do_job(self):
        print('I am walking ...')
        if isinstance(self, D):
            super(A, self).do_job()


class Z:
    def do_job(self, n):
        self.n = n
        print(f'I am counting from 1 to {self.n}:  {list(range(1, self.n + 1))}')


class B(A):
    def do_job(self, s):
        self.s = s

        super().do_job()
        print(f'I am printing your string : "{self.s}"')


class C(Z, A):
    def do_job(self, n):
        self.n = n
        super().do_job(self.n)
        print('I am jumping ...')


class D(B):
    def do_job(self, s):
        self.s = s
        super().do_job(self.s)
        print('I am speaking ...')


class E(D, C):
    def do_job(self, s, n):
        self.s = s
        self.n = n
        super().do_job(self.s, self.n)
        print('I am laughing ...')


class F(Z, B):
    def do_job(self, s, n):
        super().do_job(s, n)
        print('I am playing ...')


obja = A()
obja.do_job()

print()
objz = Z()
objz.do_job(3)

print()
print(E.mro())
obje = E()
obje.do_job('Python', 5)

print()
objf = F()
objf.do_job('Python', 6)
