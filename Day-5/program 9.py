from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def description(self):
        return ("This is a shape")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius * self.radius)
    def perimeter(self):
        return 3.14 * 2 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

circle = Circle(5)

rectangle = Rectangle(5, 5)

print(f"Area of circle: {circle.area()}")
print(f"Perimeter of circle: {circle.perimeter()}")
print(f"Circle description: {circle.description()}")

print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle parameters: {rectangle.perimeter()}")
print(f"Rectangle description: {rectangle.description()}")
