import typing
from functools import wraps
import time


def timeit(my_func):
    """timer decorator"""
    @wraps(my_func)
    def timed(*args, **kw):
        start_time = time.time()
        output = my_func(*args, **kw)
        end_time = time.time()

        print('"{}" took {:.3f} ms to execute\n'.format(my_func.__name__, (end_time - start_time) * 1000))
        return output

    return timed


@timeit
def hsg(n: int):
    """a generator for Sequence of hailstone"""
    if not isinstance(n, int):
        raise TypeError('input must be integer!')
    if n <= 0:
        raise ValueError('input must bigger than zero')
    yield n
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            yield int(n)
        else:
            n = 3 * n + 1
            yield int(n)
        hsg(n)


t1 = hsg(900)
next(t1)
next(t1)
# print(next(t1))
# print(next(t1))
# print(next(t1))
# print(next(t1))
# print(next(t1))
# print(next(t1))
# print(next(t1))
# print(next(t1))

def len_hsg(n: int):
    """a function for calculate length of sequence of hailstone"""
    try:
        cnt = 0
        x = hsg(n)
        while True:
            next(x)
            cnt += 1
    except StopIteration:
        return cnt


# l1 = len_hsg(3)
# print(l1)

@timeit
class His:
    """iterator for sequence of hailstone"""

    def __init__(self, number: int):
        self.number = number
        self.cnt = 0
        if not isinstance(self.number, int):
            raise TypeError('input must be integer!')
        if self.number <= 0:
            raise ValueError('input must bigger than zero')

    def __iter__(self):
        return self

    def __next__(self):
        self.cnt += 1
        if self.cnt == 1:
            return self.number
        while self.number > 1:
            if self.number % 2 == 0:
                self.number = self.number / 2
                return int(self.number)
            else:
                self.number = 3 * self.number + 1
                return int(self.number)
        raise StopIteration


x = iter(His(6))
next(x)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))



