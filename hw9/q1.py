import argparse
from cryptography.fernet import Fernet
import os


# part A #
def generate_key():
    """generate a secret key"""
    key = Fernet.generate_key()
    file_name = 'secret_key.txt'
    with open(file_name, 'wb') as file:
        file.write(key)
    return file_name


# part B #

class Encryption:
    """a class for encryption data and files"""

    def __init__(self, key_file_name: str):
        with open(key_file_name, 'rb') as file:
            key = file.read()
            if not isinstance(key, bytes):
                raise TypeError
        self.key = key

    def encrypt_data(self, data: str):
        f = Fernet(self.key)
        data_as_bytes = str.encode(data)
        token_res = f.encrypt(data_as_bytes)
        print('input data is encrypted!')
        return token_res

    def encrypt_file(self, file_name: str):
        f = Fernet(self.key)
        with open(file_name, 'r') as file:
            file_data = file.read()
        file_data_as_bytes = str.encode(file_data)
        token_result = f.encrypt(file_data_as_bytes)
        new_file_name = 'encrypted_' + file_name
        with open(new_file_name, 'wb') as new_file:
            new_file.write(token_result)
        print('file is encrypted: ')
        return new_file_name

def decorator(key: str, *args, **kwargs):
    """a decorative for encrypt output of a function"""
    def inner_func(func):
        res = func(*args, **kwargs)
        def encryption():
            f = Fernet(key)
            res_as_bytes = str.encode(res)
            token_res = f.encrypt(res_as_bytes)
            return token_res
        return encryption

    return inner_func

@decorator('cPpSI_hyjBlvqilhpjwWSQuQIvT0r6SRWBSNwh-Bijc=')
def hello_world():
    return 'hello world'

x = hello_world()
print(x)



# part C #
class Decryption:
    """a class for decryption data and files and edit encrypted files"""

    def __init__(self, key_file_name: str):
        with open(key_file_name, 'rb') as file:
            key = file.read()
            if not isinstance(key, bytes):
                raise TypeError
        self.key = key

    def decrypt_data(self, data: str):
        data = bytes(data, 'utf-8')
        if not isinstance(data, bytes):
            raise TypeError
        f = Fernet(self.key)
        res_as_bytes = f.decrypt(data)
        res = res_as_bytes.decode()
        print('input data decrypted:')
        return res

    def decrypt_file(self, file_name: str):
        with open(file_name, 'rb') as file:
            data = file.read()

        f = Fernet(self.key)
        res_as_bytes = f.decrypt(data)
        res = res_as_bytes.decode()
        new_file_name = 'decrypted_' + file_name
        with open(new_file_name, 'w') as new_file:
            new_file.write(res)
        print('file is decrypted: ')
        return new_file_name





if __name__ == '__main__':
    """a scrypt program for encrypt and decrypt utilities"""
    parser = argparse.ArgumentParser(description='this scrypt is for encrypt and decrypt')
    parser.add_argument('-g', '--generate', action='store_true', dest='generate',
                        help='generate a key for encryption and save in a file')
    subparser = parser.add_subparsers(dest='command')
    encrypt = subparser.add_parser('encrypt')
    decrypt = subparser.add_parser('decrypt')


    encrypt.add_argument('key', type=str, help='enter your file name of key for encrypt')
    encrypt.add_argument('-c', '--content', action='store', type=str, help='enter content for encrypt')
    encrypt.add_argument('-f', '--file', action='store',type=str, help='enter file name for encrypt')

    decrypt.add_argument('key', type=str, help='enter your file name of key for decrypt')
    decrypt.add_argument('-c', '--content', action='store', type=str, help='enter content for decrypt')
    decrypt.add_argument('-f', '--file', action='store', type=str, help='enter file name for decrypt')

    args = parser.parse_args()

    if args.generate:
        key_file = generate_key()
        print('secret key generated: ')
        print(key_file)

    if args.command == 'encrypt':

        key_file_path = args.key
        assert os.path.exists(key_file_path), 'the key file not exist!!!'
        enc1 = Encryption(key_file_path)
        if args.content:
            data_content = args.content
            res_enc = enc1.encrypt_data(data_content)
            print(res_enc)
        if args.file:
            file_path = args.file
            assert os.path.exists(file_path), 'the file not exist!!!'
            file_enc = enc1.encrypt_file(file_path)
            print(file_enc)

    if args.command == 'decrypt':
        key_file_path = args.key
        assert os.path.exists(key_file_path), 'the key file not exist!!!'
        dec1 = Decryption(key_file_path)
        if args.content:
            data_content = args.content
            res_dec = dec1.decrypt_data(data_content)
            print(res_dec)
        if args.file:
            file_path = args.file
            assert os.path.exists(file_path), 'the file not exist!!!'
            file_dec = dec1.decrypt_file(file_path)
            print(file_dec)







