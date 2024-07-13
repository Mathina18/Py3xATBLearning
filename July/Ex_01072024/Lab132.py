# Multilevel Inheritance

class Grandparent():
    key_gold = "2kg"
    def grandparent_method(self):
        return "Grandparents method"


class Parent(Grandparent):
    def parent_method(self):
        return "Parent method"


class Child(Parent):
    apple_watch = "New apple watch"
    def child_method(self):
        return "child method"


child = Child()
print(child.child_method())
print(child.parent_method())
print(child.grandparent_method())
print(child.key_gold)
print(child.apple_watch)

parent = Parent()
print(parent.parent_method())
print(parent.grandparent_method())
print(parent.key_gold)

grandparent = Grandparent()
print(grandparent.grandparent_method())
print(grandparent.key_gold)
