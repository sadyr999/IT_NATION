from math import pi

class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "fan fact"

class Square(Shape):
    def __init__(self, length):
        super(Square, self).__init__('Square')
        self.length = length
    def area(self):
        return pow(self.length, 2)
    def fact(self):
        return "fan fact 2"

class Circle(Shape):
    def __init__(self, radius):
        super(Circle, self).__init__("Circle")
        self.radius = radius
    def area(self):
        return pi * pow(self.radius, 2)

square = Square(44)
print(square.fact())
print(square.area())
circle = Circle(9999)
print(circle.fact())
print(circle.area())
