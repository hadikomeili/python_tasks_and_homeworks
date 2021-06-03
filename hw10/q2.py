import json
from q1 import phone_validation,email_validation,name_validation



class Register:
    """a class for register users"""

    def __init__(self, first_name: str, last_name: str, phone: str, password: str, email: str):
        if name_validation(first_name):
            self.first_name = first_name
        else:
            raise TypeError
        if name_validation(last_name):
            self.last_name = last_name
        else:
            raise TypeError
        if phone_validation(phone):
            self.phone = phone
        else:
            raise TypeError
        self._password = password
        if email_validation(email):
            self.email = email
        else:
            raise TypeError

    def __repr__(self):
        return f'{self.first_name=}\n{self.last_name=}\n{self.phone=}\n{self._password=}\n{self.email=}'

def user_dictionary(user: Register):
    user_dict = {}
    # user_list = []
    user_dict['first_name'] = user.first_name
    user_dict['last_name'] = user.last_name
    user_dict['phone'] = user.phone
    user_dict['password'] = user._password
    user_dict['email'] = user.email
    return user_dict

def save_in_json(data):
    with open('user.json', 'w') as f:
        json.dump(data, f)
        return 'user.json'


def register_by_json(file_path: str):
    with open(file_path, 'r') as file:
        data = json.load(file)
        data = data[0]
    user1 = Register(data['first_name'], data['last_name'], data['phone'], data['password'], data['email'])
    return user1

if __name__ == '__main__':
    users = []
    u1 = Register('komeil', 'komeili', '09159600000', '123', 'komeili.hadi@gmail.com')
    x = user_dictionary(u1)
    users.append(x)
    
    res = save_in_json(users)
    print('users saved in:', res)

    final_result = register_by_json(res)
    print(final_result)

