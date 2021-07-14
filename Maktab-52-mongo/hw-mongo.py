from pymongo import MongoClient

client = MongoClient('localhost')
db = client['mongo-hw']
product_collection = db['products']
markup_collection = db['markups']
commission_collection = db['commission']
user_collection = db['users']


#---- part 1
def calculate_markup_percent(product_type:str, product_number:int):
    myquery = {"product_type": product_type}
    my_markup = markup_collection.find(myquery)
    for data in my_markup:
        upper_cost = data["upper_cost"]
        lower_cost = data["lower_cost"]
        lower_count = data["lower_count"]

    if product_number == 1:
        markup = upper_cost
    elif product_number > lower_count:
        markup = lower_cost
    else:
        markup = ((product_number/lower_count)*(upper_cost - lower_cost))+lower_cost

    return markup


# x = calculate_markup_percent("2", 5)
# print(x)

#-------------------------------------
# ---- part 2

def calculate_product_price(product_type:str, count:int, user_id:int=None):

    my_query = {"product_type":product_type}
    my_product = product_collection.find(my_query)
    # product_name = ''
    # price = 0
    # total_price = 0
    # total_with_commission = 0
    # discount = 0
    username = {}
    for p in my_product:
        product_name = p["name"]
        price = p["price"]
        unit = p["unit"]
        com_group = p["commission_groups"]
        for group in com_group:
            group_query = {"group_name":group}
            x = commission_collection.find(group_query)
            for com in x:
                if com["unit"] == unit:
                    my_commission = com
                    cost = my_commission["cost"]
                    users = my_commission["users"]

    total_price = count * price
    if unit == "Dollar":
        discount = count * cost
    else:
        discount = total_price * cost
    total_with_commission = total_price - discount

    for u in users:
        if u == user_id:
            user_query = {"userid":u}
            user_info = user_collection.find(user_query)
            for user in user_info:
                username["first name"] = user["first_name"]
                username["last name"] = user["last_name"]
        else:
            pass

    return f'{product_name=} , {total_price=} , {total_with_commission=} , {discount=} , {username=}'


res = calculate_product_price("1", 10)
print(res)