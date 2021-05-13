import os

def print_file_generator(dir_path: str):
    """a generator to print files of directory"""
    if not os.path.isdir(dir_path):
        raise ValueError
    for root, dirs, files in os.walk(dir_path):
        file_number = len(files)
        cnt = 0
        for file in files:
            if cnt <= file_number:
                cnt += 1
                yield print(file)
            else:
                raise Exception




try:
    print('WELCOME\nthis is a program to generat file name of a directory')
    directory_path = input('enter a directory:\n')
    g = print_file_generator(dir_path=directory_path)
    answer = 'y'
    while answer.lower() == 'y':
        next(g)
        answer = input('you want see the next file name?\ny or n\n')
except ValueError:
    print("Invalid Directory!!!")
except Exception:
    print("all of files in this directory is printed")
except:
    print("UNEXPECTED ERROR!!! ==> PLEASE TRY AGAIN")
