import os


def print_specific_files(format: str, directory: str):
    """this function by getting a format and directory, print names of files with that format in that directory"""
    if not os.path.isdir(directory):
        raise ValueError
    if not format.startswith('.'):
        format = '.' + format
    for root, dirs, files in os.walk(directory):
        answer_list = []
        for file in files:
            if file.endswith(format):
                answer_list.append(file)
    return answer_list



try:
    print("WELCOME\nfile finder program based on format")
    directory_path = input('enter intended directory:\n')
    format = input('enter selected format:\n')
    x = print_specific_files(directory=directory_path, format=format.lower())
    if len(x) == 0:
        print("no files with selected format exist in this directory!!!")
    else:
        print('this is list of files with selected format in this directory:\n')
        print(x)
except ValueError:
    print("Invalid Directory!!!")
except:
    print("UNEXPECTED ERROR!!! ==> PLEASE TRY AGAIN")


