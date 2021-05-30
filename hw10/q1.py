import re


def name_validation(name: str):
    assert isinstance(name, str), 'invalid input ... name must be string'
    name_format = r'^([a-zA-Z_]){5,14}$'
    if re.search(name_format, name):
        return True
    else:
        return False


# name1 = input('enter your name: ')
# res = name_validation(name1)
# print(res)


def email_validation(email: str):
    assert isinstance(email, str), 'invalid input ... email must be string'
    email_format = r'^([a-zA-Z]+)([._+a-zA-Z0-9]*)(@{1})([a-zA-Z]+)([._a-zA-Z0-9]*)([.]{1})([a-zA-Z]+)$'
    if re.search(email_format, email):
        return True
    else:
        return False


#
# email1 = input('enter email: ')
# em = email_validation(email1)
# print(em)


def phone_validation(phone: str):
    assert isinstance(phone, str), 'invalid input ... phone number must be string'
    phone_format = r'(^09)([\d]){9}$|(^\+989)([\d]){9}$'
    if re.search(phone_format, phone):
        return True
    else:
        return False


phone1 = input('enter phone number: ')
pv = phone_validation(phone1)
print(pv)
