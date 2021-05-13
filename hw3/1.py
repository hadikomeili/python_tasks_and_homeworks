class User:

    def __init__(self, name: str, phone: int):
        self.name = name
        self.phone = phone

class BankAccount:

    def __init__(self, owner: User, account_balance: float, min_account_balance = 2000):
        self.owner_name = owner.name
        self.__account_balane = account_balance
        self.min_account_balance = min_account_balance

    def deposit(self, amount: float):
        amount = float(amount)
        assert amount > 0
        self.__account_balance += amount
        print('Deposit was made to the account.')
        return self.__account_balance

    def withdrawal(self, amount: float):
        x = self.__checking(amount)
        if x == True:
            self.__account_balance -= amount
            print('Withdrawal was made from the account.')
        else:
            print('Account balance is not enough for this operation.')
        return self.__account_balance

    def __str__(self):
        return f'owner: {self.owner_name} , account balance: {self.__account_balane}'


user1 = User('Jacob', 2546528)
bank_account1 = BankAccount(user1, 250000)
print(bank_account1)
bank_account1.deposit(12000)
print(bank_account1)
bank_account1.withdrawal(15000)
print(bank_account1)
bank_account1.withdrawal(2900000)
print(bank_account1)