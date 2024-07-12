# Web Automation - Selenium
# Page - You are going automate

class VWOLogin:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "hbanis8@gmail.com" and self.password == "Pass1234":
            print("Allowed to enter")
        else:
            print("Not allowed")


email = str(input("Enter the email:"))
password = str(input("Enter the password:"))
mathina = VWOLogin(email, password)
mathina.login_confirm()
