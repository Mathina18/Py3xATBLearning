# Multiple Inheritance
# Probelm - Diamond Problem - Java
# Python - Multiple Inheritance
# F,M -> S

class Father:
    def father_money(self):
        return "5"

    def home(self):
        return "This is from father"


class Mother:
    def mother_money(self):
        return "2"

    def home(self):
        return "This is from mother"



class son(Father, Mother):
    def son(self):
        pass


son = son()
print(son.father_money())
print(son.mother_money())
print(son.home())
