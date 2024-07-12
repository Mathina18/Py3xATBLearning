#  Class Variable.
#  Method
#      # Public - Variable - Don't Mention anything
#      # Protected - _
#      # Private - __
#  Inheritance
# Polymorphism
# Abstraction,
# Encapsulation
# Static Method,
# Variables

class Person:
    name = "mathina"
    age = None

    def walk(self):
        a = 10 #local variable
        print("I am a method")
        print("hi", self.age)


person = Person()
person.walk()
