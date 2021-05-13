

def counter_func(file_path: str, level: str):
    level_list = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'FATAL', 'CRITICAL')
    if level.upper() in level_list:
        with open(file_path) as file:
            data = file.read()
            # print(data)
            res = data.count(level.upper())
        return res
    else:
        print('the inputs is incorrect')


x = counter_func('person.log', 'error')
print(x)