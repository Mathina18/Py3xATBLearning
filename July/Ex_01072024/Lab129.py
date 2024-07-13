# Inheritance
# Acquire the Attributes and Behaviour
# Data members and Methods

# 3BHK Hourse -F -> Inheritance - Son -
# concept in object-oriented programming (OOP)
# that allows a class (child class) to inherit attributes and methods
# from another class (parent class)

# Types of Inheritance

# Single - 80%  - # API, Web Automation - 80% -> Single
# Multiple
# Multi level
# Hybrid
# Hierarchical

#single

class Grandparent:
    key = "123"
    def grandparent_method(self):
        return "grandparents method"


class Parent(Grandparent):
    def parent_method(self):
        return "Parents method"


Grandfather = Grandparent()
Grandfather.grandparent_method()

Father = Parent()
print(Father.grandparent_method())
print(Father.parent_method())
print(Father.key)


