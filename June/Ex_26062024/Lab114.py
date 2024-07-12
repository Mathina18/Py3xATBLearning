class Calc:

    def __init__(self):
        print("Hello DC")

    def sum(self,a,b):
        return a+b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


object_ref = Calc()
output = object_ref.sum(3,4)
output1 = object_ref.sub(3,4)
output2 = object_ref.mul(3,4)
output3 = object_ref.div(3,4)
print(output)
print(output1)
print(output2)
print(output3)
