#shape calculator
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height
circle = Circle(5)
rectangle = Rectangle(10, 20)
triangle = Triangle(8, 12)

print("Area of circle:", circle.calculate_area())
print("Area of rectangle:", rectangle.calculate_area())
print("Area of triangle:", triangle.calculate_area())
