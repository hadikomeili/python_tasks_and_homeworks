import os


def my_func(dir_path: str):
    if os.path.isdir(dir_path):
        list_dir = os.listdir(dir_path)
        # print(list_dir)
        res = 0
        for items in list_dir:
            items_path = dir_path + f'\{items}'
            # print(items_path)
            if os.path.isfile(items_path):
                file_extension = os.path.splitext(items)
                if len(file_extension[0]) > 5:
                    # print(items)
                    space = os.path.getsize(items_path)
                    res += space
                else:
                    pass
            else:
                pass
        print('result = ', res)
    else:
        print('This is not a Valid Directory Path')


path = input('enter a directory path: \n')
my_func(path)
