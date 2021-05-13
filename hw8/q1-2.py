import argparse


def avg_func(grades: list):
    grades_sum = 0
    for grade in grades:
        if 0 <= int(grade) <= 20:
            grades_sum += int(grade)
        else :
            raise ValueError('the grades must be between 0 to 20 !!!')
    average = grades_sum / len(grades)
    return average

if __name__ == '__main__':
    """a script with argparse for calculate average of grades"""
    parser = argparse.ArgumentParser(description="calculate average with Optional decimal!")
    parser.add_argument('-g', '--grades', metavar='GRADES', action='append', nargs='*', required=True, dest='grades',
                        help='enter the grades with space between them', type=float)

    parser.add_argument('-f', '--float', metavar='FLOAT', action='store', default='2', dest='float', type=int)


    args = parser.parse_args()
    answer = avg_func(*args.grades)
    selected_float = '%.' + str(args.float) + 'f'
    print(selected_float % answer)
