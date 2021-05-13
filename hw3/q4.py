class Owner:

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

class BankAccount:

    def __init__(self, owner: Owner, account_balance:float, min_account_balance: float):
        self.owner = owner
        self.account_balance = account_balance
        self.min_account_balance = min_account_balance

    def __checking(self, amount: float):
        x = self.account_balance - amount
        if x >= self.min_account_balance:
            flag = True
        else:
            flag = False
        return flag

    def deposit(self, amount: float):
        self.account_balance += amount
        print('Deposit was made to the account.')
        return f'Account Balance = {self.account_balance}'

    def withdrawal(self, amount: float):
        x = self.__checking(amount)
        if x == True:
            self.account_balance -= amount
            print('Withdrawal was made from the account.')
        else:
            print('Account balance is not enough for this operation.')
        return f'Account Balance = {self.account_balance}'

    def transfer(self, other_account, amount: float):
        x = self.__checking(amount)
        if x == True:
            self.account_balance -= amount
            other_account.account_balance += amount
            print('Transfer done.')
        else:
            print('Account balance is not enough for this operation.')
        return f'Account Balance = {self.account_balance} , Other Account Balance = {other_account.account_balance}'


owner1 = Owner('Bary', 'Allen')
account1 = BankAccount(owner1, 50000, 2000)
y = account1.deposit(7000)
print(y)
x = account1.withdrawal(60000)
print(x)
z = account1.withdrawal(17000)
print(z)
owner2 = Owner('Lari', 'King')
account2 = BankAccount(owner2, 25000, 1000)
x2 = account1.transfer(account2, 5000)
print(x2)
y2 = account2.transfer(account1, 30000)
print(y2)