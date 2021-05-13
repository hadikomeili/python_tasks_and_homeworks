# q2 in hw6



class GetNumber:

    def __init__(self, input: str):
        self.input = input

    def Normalize(self):
        operators = ('+', '-', '*', '/')
        self.input = self.input.replace(' ', '')
        count_operators = 0
        for item in operators:
            count_operators += self.input.count(item)
            if item in self.input:
                temp_operator = item
        if count_operators > 1 or count_operators == 0:
            raise InputError
        elif count_operators == 1:
            numbers_list = self.input.split(temp_operator)
            for x in numbers_list:
                if not x.isnumeric():
                    raise InputError
            if len(numbers_list) == 2:
                numbers = tuple(numbers_list)
                # print(numbers)
            else:
                numbers = []
                raise InputError
        return [numbers, temp_operator]

    def CalculateOutput(self, numbers: tuple, operator: str):
        # operator = eval(operator)
        res = eval(str(numbers[0] + operator + numbers[1]))
        return res


def main():
    print('WELCOME\nThis program get 2 numbers and 1 operator as string and return result.')
    user_input = input('enter your favorite input:\n')
    ins1 = GetNumber(user_input)
    temp_result = ins1.Normalize()
    final_result = ins1.CalculateOutput(temp_result[0], temp_result[1])
    print('the result is ready to show.........\n')
    print(f'{final_result= }')


class InputError(Exception):
    pass


try:
    main()
except InputError:
    print('Error -> The input is wrong!!!\nPlease try again...\n')

except:
    print('Sorry, unexpected error occurred.')
