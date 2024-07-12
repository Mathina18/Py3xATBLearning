class Myclass:
    def __init__(self):
        self.name = "Mathina"
        self.email = "hbanis8@gmail.com"

    def public_fn(self):
        print("I am public function")

    def __private_fn(self):
        print("I am not accessible until cal in another function")

    def public_fn_private(self):
        self.__private_fn()
        print(self.email)


a = Myclass()
a.public_fn()
a.public_fn_private()
