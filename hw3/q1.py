class Triangle:

    def __init__(self, A, B, C):
        self.A: tuple = A
        self.B: tuple = B
        self.C: tuple = C


    def area(self):
        s = (1 / 2) * abs((self.A[0]*(self.B[1] - self.C[1]) + (self.B[0]*(self.A[1] - self.C[1]))
                + (self.C[0]*(self.A[1] - self.B[1]))))
        if s == 0:
            s = 'THIS IS NOT A TRIANGLE'
        return f'The area is = {s} '

    @staticmethod
    def __sides_length(A:tuple, B:tuple):
        __a = ((A[0] - B[0])**2 + (A[1] - B[1])**2) ** 0.5
        return __a

    def sides(self):
        a = Triangle.__sides_length(self.A, self.B)
        b = Triangle.__sides_length(self.B, self.C)
        c = Triangle.__sides_length(self.A, self.C)
        return f'side a = {a:.2f} , side b = {b:.2f} , side c = {c:.2f}'

    def perimeter(self):
        p = Triangle.__sides_length(self.A, self.B) + Triangle.__sides_length(self.A, self.C) + Triangle.__sides_length(self.B, self.C)
        return f'The perimeter is = {p:.2f} '

    def triangle_type(self):
        a = Triangle.__sides_length(self.A, self.B)
        b = Triangle.__sides_length(self.B, self.C)
        c = Triangle.__sides_length(self.A, self.C)
        sides_sorted = sorted([a, b, c])
        if a == b == c :
            res = 'متساوی الاضلاع'
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b!=a):
            res = 'متساوی الساقین'
        elif sides_sorted[0]**2 + sides_sorted[1]**2 == sides_sorted[2]**2 :
            res = 'قائم الزاویه'
        else :
            res = 'نامشخص'
        return f'Type of this triangle is: {res}'

    def center_of_gravity(self):
        x = (self.A[0] + self.B[0] + self.C[0])/3
        y = (self.A[1] + self.B[1] + self.C[1])/3
        return f'The center of gravity is : ({x:.2f}, {y:.2f})'



tri1 = Triangle((0,0),(0,2),(1,0))
print(tri1.area())
print(tri1.sides())
print(tri1.perimeter())
print(tri1.triangle_type())
print(tri1.center_of_gravity())