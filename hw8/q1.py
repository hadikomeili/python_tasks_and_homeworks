import sys


if __name__ == '__main__':
    """a script for calculate average of grades!!!"""
    args = sys.argv
    grades_list = args[1:]
    grades_sum = 0
    if len(grades_list) == 1 and grades_list[0] == '-h':
        print('a script for calculate average of grades.\nplease enter the grades with space between them.')
    elif len(grades_list) != 0 :
        for grade in grades_list:
            grades_sum += int(grade)
        avrage = grades_sum / len(grades_list)
        print(f'{avrage = }')
    else:
        print('ERORR => no grade is entered!!!')


