# Method Overriding - Same name in the parent and child
# child always override the parent functions
# super means call my parent function


class Father:
    def home(self):
        print("1BHK")


class son(Father):
    def home(self):
        print("3BHK")
        super().home()


son = son()
son.home()