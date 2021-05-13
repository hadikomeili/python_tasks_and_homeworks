from num2words import num2words


def is_primal(n: int) -> bool:
    """checking for being primal"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def remainder(n: int):
    """a decorator for returning remainder of multiplication 2 numbers to n"""

    def inner_func(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs) % n
            return res

        return wrapper
    return inner_func


def string_p(func):
    """decorator to print a number to string"""

    def inner_func(*args):
        multiply_res = func(*args)
        string_res = num2words(multiply_res)
        return f'output("the result is {string_res}")'

    return inner_func


class MultiplyPrimeNumbers:
    """multiply 2 primal numbers"""

    def __init__(self, first_number: int, second_number: int):
        self.first_number = first_number
        self.second_number = second_number
        assert isinstance(self.first_number, int), f'the number is invalid! => {self.first_number}'
        assert isinstance(self.second_number, int), f'the number is invalid! => {self.second_number}'
        assert is_primal(self.first_number), f'the number is not Primal!!! => {self.first_number}'
        assert is_primal(self.second_number), f'the number is not Primal!!! => {self.second_number}'

    @remainder(4)
    def multiplication(self):
        """multiply 2 primal numbers
        :param -> 2 int arguments(primal numbers)
        :return hasel zarb 2 adad -> int"""
        result = self.first_number * self.second_number
        return result

    @string_p
    def print_res(self):
        res = self.first_number * self.second_number
        return res


ins1 = MultiplyPrimeNumbers(3, 7)
print(ins1.multiplication())
print(ins1.print_res())
