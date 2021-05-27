import argparse
from cryptography.fernet import Fernet

# part A #
def generate_key():
    """generate a secret key"""
    key = Fernet.generate_key()
    file_name = 'secret_key.txt'
    with open(file_name, 'wb') as file:
        file.write(key)

# part B #

class Encryption:
    """a class for encryption data and files"""
    def __init__(self):
        self.key = Fernet.generate_key()


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
        with open(file_name, 'wb') as new_file:
            new_file.write(token_result)
        return print(f'{file_name} is encrypted now!')

    def secret_key(self):
        with open('secret_key.txt', 'wb') as f:
            f.write(self.key)

# part C #
class Decryption:
    """a class for decryption data and files and edit encrypted files"""
    def __init__(self, key: bytes):
        if not isinstance(key, bytes):
            raise TypeError
        self.key = key

    def decrypt_data(self, data: bytes):
        if not isinstance(data, bytes):
            raise TypeError
        f = Fernet(self.key)
        res_as_bytes = f.decrypt(data)
        res = res_as_bytes.decode()
        print('input data decrypted!')
        return res

    def decrypt_file(self, file_name: str):
        with open(file_name, 'rb') as file:
            data = file.read()

        f = Fernet(self.key)
        res_as_bytes = f.decrypt(data)
        res = res_as_bytes.decode()
        with open(file_name, 'w') as new_file:
            new_file.write(res)
        return print(f'{file_name} is decrypted now!')


# f = Fernet(key)
# token = f.encrypt(b"my deep dark secret 255")
# print(token)
# x = f.decrypt(token)
# print(x)


# ins1 = Encryption()
# ins1.encrypt_file('test.txt')
# ins1.secret_key()

# with open('secret_key.txt', 'rb') as s:
#     key = s.read()
# ins2 = Decryption(key)
# ins2.decrypt_file('test.txt')


if __name__ == '__main__':
    """a scrypt program for encrypt and decrypt utilities"""
    parser = argparse.ArgumentParser(description='this scrypt is for encrypt and decrypt')
    parser.add_argument('-g', '--generate', metavar='GENERATE_KEY', dest='generate', default=None, action='store',
                        help='generate a key for encryption and save in a file')
    # parser.add_argument('-s', '--save', metavar='SAVE_IN_FILE', dest='save', default=None, action='store',
    #                     help='save generated key in a file')
    parser.add_argument('-e', '--encrypt', metavar='ENCRYPT', dest='encrypt', action='store',
                        help='encrypt ')