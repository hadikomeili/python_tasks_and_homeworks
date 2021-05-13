import os


class BackUpOpen:
    """a class for backuping opening file """
    def __init__(self, file_path: str, mode: str= 'r'):
        self.file_path = file_path
        self.mode = mode
        assert self.mode in ('r', 'rb', 'r+', 'w', 'wb', 'w+', 'wb+', 'a', 'ab', 'a+', 'ab+'), 'invalid input!!!'
        assert os.path.isdir(self.file_path) or os.path.isfile(self.file_path), 'invalid input!!!'

    def read(self):
        if self.mode == 'r' or 'a' or 'w' or 'r+' or 'w+' or 'a+':
            with open(self.file_path, 'r') as f:
                res = f.read()
        elif self.mode == ('rb' or 'wb' or 'wb+' or 'ab' or 'ab+'):
            with open(self.file_path, 'rb') as f:
                res = f.read()
        return res

    def write(self, text: str):
        with open(self.file_path, self.mode) as f:
            f.write(text)

    def __enter__(self):
        # if self.mode == ('r' or 'a' or 'w' or 'r+' or 'w+' or 'a+'):
        with open(self.file_path, 'r') as f:
            content = f.read()
            with open('backupfile.txt', 'w') as new_f:
                new_f.write(content)
        # elif self.mode == ('rb' or 'wb' or 'wb+' or 'ab' or 'ab+'):
        #     with open(self.file_path, 'rb') as f:
        #         content = f.read()
        #         with open('backupfile.txt', 'wb') as new_f:
        #             new_f.write(content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val or exc_type:
            print('Error => the back up file is replaced.')
            # if self.mode == ('r' or 'a' or 'w' or 'r+' or 'w+' or 'a+'):
            with open('backupfile.txt', 'r') as new_f:
                backup_content = new_f.read()
                with open(self.file_path, 'w') as f:
                    f.write(backup_content)
            # elif self.mode == ('rb' or 'wb' or 'wb+' or 'ab' or 'ab+'):
            #     with open('backupfile.txt', 'rb') as new_f:
            #         backup_content = new_f.read()
            #     with open(self.file_path, 'wb') as f:
            #         f.write(backup_content)
        else:
            pass
        return True


with BackUpOpen('testq3.txt') as f:
    f.write('\ngood night')
    # f.write(25)
