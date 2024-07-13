# Polymorphism
# Polymorphism allows objects of
# different classes to be treated as
# objects of a common superclass.

# Pramod -> Mentor, Husband, Brother.
# Object -Method -> Mother, Matenal She is, sister, parent -

# Method overriding

class Shape():
    def area(self):
        print("Area of the shape:")


class rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
       return self.length * self.width


class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape = Shape()
shape.area()

rectangle = rectangle(3,4)
print("Rectangle:", rectangle.area())

circle = circle(5)
print("Circle:",circle.area())




