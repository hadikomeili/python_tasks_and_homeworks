import random
import argparse


def random_number_func(start_num: int, end_num: int):
    if end_num > start_num:
        answer = random.randint(start_num, end_num)
    else:
        raise TypeError
    return answer


def guess_func(random_number: int, guess: int, start: int, end: int):
    counter = 0
    x = int(input('enter your guess:\n'))
    counter += 1
    if start <= x <= end:
        while counter < guess:
            if x > random_number:
                x = int(input('enter lower number!\n'))
                counter += 1
            elif counter < random_number:
                x = int(input('enter higher number!\n'))
                counter += 1
            if x == random_number:
                print('!!!congratulation!!!\nyou guess right!')
                break
        else:
            raise TimeoutError
    else:
        raise ValueError


try:
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description="Guess Number!!!")

        parser.add_argument('-f', '--from_number', metavar='FROM_NUMBER', dest='from_number', type=int, default=0,
                            action='store', help='enter start number for create random number')
        parser.add_argument('-t', '--to_number', metavar='TO_NUMBER', dest='to_number', type=int, required=True,
                            action='store', help='enter end number for create random number')
        parser.add_argument('-g', '--guesses', metavar='NUMBER_OF_GUESSES', dest='guess', type=int, required=True,
                            action='store', help='enter number of guesses')

        args = parser.parse_args()
        r_number = random_number_func(start_num=args.from_number, end_num=args.to_number)
        guess_func(random_number=r_number, guess=args.guess, start=args.from_number, end=args.to_number)
except TimeoutError:
    print('you loose, your guesses are incorrect all and your chance is up!!!')
except TypeError:
    print('invalid inputs!!!')
except ValueError:
    print('your guess is invalid!!! (out of range)')
# except:
#     print('sorry! unexpected error.')
