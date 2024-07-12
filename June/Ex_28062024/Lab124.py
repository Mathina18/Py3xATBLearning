class VWOLogin:
    def __init__(self, email, password, name):
        self.__email = email
        self.__password = password
        self.name = name
        self.__name = "abc"

    def login_confirm(self):
        if self.__email == "hbanis8@gmail.com" and self.__password == "Pass1234":
            print("Allowed")
        else:
            print("not allowed")


page1 = VWOLogin("hbanis8@gmail.com", "Pass1234", "Mathi")
page1.login_confirm()
print(page1.name)