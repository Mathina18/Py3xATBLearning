class Bankaccount:

    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print("your balance is:" , self.balance)


sbi = Bankaccount()
print(sbi.balance)
sbi.deposit(100)
sbi.show_balance()
sbi.withdraw(50)
sbi.show_balance()
sbi.deposit(55)
sbi.show_balance()

