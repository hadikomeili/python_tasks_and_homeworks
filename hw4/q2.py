from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def drawing(self):
        pass

    @staticmethod
    def concat_area(rec_list: list):
        sum_area = 0
        for recs in rec_list:
            sum_area += recs[0] * recs[1]
        return sum_area


class Rectangle(Shape):

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def area(self):
        return self._x * self._y

    @area.setter
    def area(self, x, y):
        if x > 0 and y > 0 and isinstance(x, int) and isinstance(y, int):
            self._x = x
            self._y = y
        else:
            print('Enter a valid numbers sides for rectangle!!!')

    @property
    def perimeter(self):
        return 2 * (self._x + self._y)

    @perimeter.setter
    def perimeter(self, x, y):
        if x > 0 and y > 0 and isinstance(x, int) and isinstance(y, int):
            self._x = x
            self._y = y
        else:
            print('Enter a valid numbers sides for rectangle!!!')

    def drawing(self):
        pass

    def concat_area(rec_list: list):
        pass

class Square(Shape):

    def __init__(self, a):
        self._a = a

    def drawing(self):
        for i in range(self._a):
            for j in range(self._a):
                print('*', end ='  ')
            print()

    def area(self):
        pass

    def perimeter(self):
        pass

    @staticmethod
    def draw_concat(sq_list: list):
        for sq in sq_list:
            Square.drawing(sq)



rec = Rectangle(1, 4)
z = rec.perimeter
print(z)
a = rec.area
print(a)
rec2 = Rectangle(2,3)

list_of_recs = [rec2, rec]
c = Rectangle.concat_area(list_of_recs)
print(c)

s1 = Square(3)
s1.drawing()
print('\n')
s2 = Square(5)
s3 = Square(2)
sq_list = [s1, s2, s3]
d = Square.draw_concat(sq_list)
