# Hybrid Inheritance

# multiple types of inheritance,
# such as single,
# multiple, and
# multilevel inheritance.

class A:
    def methodA(self):
        return "A"


class B(A):
    def methodB(self):
        return "B"


class C(A):
    def methodC(self):
        return "C"


class D(C,B): # Multiple, Multilevel - MRO(Method Resolution Order - First
    def methodD(self):
        return "D"


d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())
