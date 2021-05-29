import os
from cryptography.fernet import Fernet

class EncryptionOpen:
    """a class for editing encrypted files """
    def __init__(self, file_path: str, key_path: str , mode: str= 'rb'):
        assert mode in ('r', 'rb', 'r+', 'w', 'wb', 'w+', 'wb+', 'a', 'ab', 'a+', 'ab+'), 'invalid input!!!'
        assert os.path.isdir(file_path) or os.path.isfile(file_path), 'invalid input!!!'
        assert os.path.isdir(key_path) or os.path.isfile(key_path), 'key path not find!!!'
        self.file_path = file_path
        self.mode = mode
        self.key_path = key_path
        with open(self.key_path, 'rb') as f_k:
            self.key = f_k.read()
            assert isinstance(self.key, bytes), 'invalid secret key !!!'

    def read(self):
        with open(self.file_path, 'rb') as file:
            data = file.read()
        f = Fernet(self.key)
        res_as_bytes = f.decrypt(data)
        res = res_as_bytes.decode()
        return res

    def write(self, text: str):
        with open(self.file_path, self.mode) as f:
            f.write(text)

    def __enter__(self):
        
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

ins1 = EncryptionOpen('encrypted_test.txt', 'secret_key.txt')
x = ins1.read()
print(x)