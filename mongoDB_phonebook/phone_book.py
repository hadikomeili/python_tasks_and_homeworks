from pymongo import MongoClient

client = MongoClient(port=27017)
db = client.contact


def insert_new_contact():
    contact = {"first_name": input("please enter first name: "), "last_name": input("please enter last name: ")}
    number_of_phones = int(input("please enter the number of this person's phones: "))
    for i in range(number_of_phones):
        key = input("please enter key for phone number: ")
        key = key.lower()
        contact[key] = input(f"please enter phone number for {key}: ")

    return db.phone_book.insert_one(contact)


def show_phone_book():
    for x in db.phone_book.find():
        print(x)


def delete_element(key:str, value):
    key = key.lower()
    my_query = {key: value}
    db.phone_book.delete_one(my_query)
    return key


def update_element(key:str, old_value, new_value):
    key = key.lower()
    my_query = {key: old_value}
    new_values = {"$set": {key: new_value}}
    db.phone_book.update_one(my_query, new_values)
    return key

def find_contact(key:str, value):
    key = key.lower()
    my_query = {key: value}
    res = db.phone_book.find(my_query)
    for x in res:
        print(x)


## for add new row (contact)
# insert_new_contact()
## for show all data (phone book)
#show_phone_book()
## for update
# update_element('home', '05632323232', '02155555555')
## for delete
# delete_element("mobile", "09123456789")
## for search
find_contact('last_name','koochaki')

# show_phone_book()
