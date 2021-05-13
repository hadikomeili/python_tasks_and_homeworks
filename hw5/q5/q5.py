import pickle
import dill


class User:

    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def __repr__(self):
        return f"{self.id}: {self.first_name} {self.last_name} <{self.phone}>"

    @classmethod
    def fullname(cls, file_path):
        list_fullname = []
        # file_path = 'users.pickled'
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
            for user in data:
                full_name = user.first_name + ' ' + user.last_name
                list_fullname.append(full_name)
            # print(list_fullname)
        output_file_3 = 'output-q-5-3.txt'
        return dill.dump(list_fullname, open(output_file_3, mode='wb'))


file_path = 'users.pickled'
with open(file_path, 'rb') as f:
    list_of_users = pickle.load(f)
    # print(list_of_users)


new_list = sorted(list_of_users, key=lambda x: x.id)
# print(new_list)
output_file = 'output-q-5-1.txt'
with open(output_file, 'wb') as out_f:
    pickle.dump(new_list, out_f)


new_list_2 = []
for user in list_of_users:
    if user.phone.startswith('0919'):
        new_list_2.append(user)


output_file_2 = 'output-q-5-2.txt'
with open(output_file_2, 'wb') as out_f2:
    pickle.dump(new_list_2, out_f2)


User.fullname('users.pickled')
