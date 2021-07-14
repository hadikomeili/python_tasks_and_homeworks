from pymongo import MongoClient

client = MongoClient('localhost')
db = client['mongo-hw']
product_collection = db['products']
markup_collection = db['markups']
commission_collection = db['commission']
user_collection = db['users']


product_list = [
       {
           "type": "1",
           "name": "shirt",
           "price": 30,
           "unit": "Dollar",
           "commission_groups": ["A", "B"]
       },
       {
           "type": "2",
           "name": "pants",
           "price": 50,
           "unit": "Dollar",
           "commission_groups": ["A", "C"]
       },
       {
           "type": "3",
           "name": "shoes",
           "price": 80,
           "unit": "Dollar",
           "commission_groups": ["B"]
       },
       {
           "type": "4",
           "name": "hat",
           "price": 20,
           "unit": "Dollar",
           "commission_groups": []
       }
],

markup_list = [
    {
        "product_type": "1",
        "lower_cost": 10,
        "upper_cost": 20,
        "unit": "percent",
        "lower_count": 10
    },
    {
        "product_type": "2",
        "lower_cost": 15,
        "upper_cost": 20,
        "unit": "percent",
        "lower_count": 10
    },
    {
        "product_type": "3",
        "lower_cost": 10,
        "upper_cost": 15,
        "unit": "percent",
        "lower_count": 5
    },
    {
        "product_type": "4",
        "lower_cost": 10,
        "upper_cost": 30,
        "unit": "percent",
        "lower_count": 20
    },
]

commission_list = [
    {
        "group_name": "A",
        "cost": 5,
        "unit": "percent",
        "users": [1001, 1002, 1003, 1005]
    },
    {
        "group_name": "B",
        "cost": 3,
        "unit": "Dollar",
        "users": [1001, 1003, 1006]
    },
    {
        "group_name": "C",
        "cost": 7,
        "unit": "percent",
        "users": [1001, 1002, 1004]
    }
]

user_list = [
    {
        "userid": 1001,
        "first_name": "Mohsen",
        "last_name": "Bayat",
    },
    {
        "userid": 1002,
        "first_name": "Sobhan",
        "last_name": "Taghadosi",
    },
    {
        "userid": 1003,
        "first_name": "Javad",
        "last_name": "Jafari",
    },
    {
        "userid": 1004,
        "first_name": "Masoud",
        "last_name": "Hosseini",
    },
    {
        "userid": 1005,
        "first_name": "Hassan",
        "last_name": "Zand",
    },
    {
        "userid": 1006,
        "first_name": "Ali",
        "last_name": "Ebadi",
    }
]



# p = product_collection.insert_many(*product_list)
#
# for markup in markup_list:
#     markup_collection.insert_one(markup)
#
# for com in commission_list:
#     commission_collection.insert_one(com)
#
# for user in user_list:
#     user_collection.insert_one(user)


for coll in db.list_collection_names():
    print(coll)


print(user_collection.count())