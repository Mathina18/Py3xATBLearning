class Car:
    name = None

    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected"
        self.__private_var = "pass123"

    def __private_method(self):
        print("protected")

    def public_method(self):
        self.__private_method()
        if self.__private_var == "123":
            print("H,123")
        print("I am allowed public")


hondacity = Car()
hondacity.public_method()
