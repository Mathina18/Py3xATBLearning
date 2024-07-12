class Bankaccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, balance):
        self.balance += balance

    def __withdraw(self, balance):
        self.balance -= balance

    def __show_balance(self):
        print("your balance is:", self.balance)

    def if_you_are_auth(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("not allowed")

    def if_you_are_auth_user(self, auth, balance):
        if auth:
            self.__withdraw(balance=balance)
        else:
            print("not allowed")


sbi = Bankaccount()
print(sbi.balance)
sbi.deposit(100)

secret_pass = input("Enter your pin to see the balance:")
if secret_pass == "1234":
    sbi.if_you_are_auth(True)
else:
    sbi.if_you_are_auth(False)

secret_pass = input("Enter your pin to withdraw:")
withdraw_amount = int(input("Enter the amount to withdraw:"))
if secret_pass == "1234":
    sbi.if_you_are_auth_user(True, balance=withdraw_amount)
    sbi.if_you_are_auth(True)
else:
    sbi.if_you_are_auth(False)
