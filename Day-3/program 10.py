


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

    def combine(self,other):
        new_area = self.area() + other.area()
        new_width = self.width + other.width
        new_height = new_area / new_width
        return Rectangle(new_width, new_height)

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

rect1 = Rectangle(10, 20)
rect2 = Rectangle(10, 20)
combined_rect = rect1.combine(rect2)
print(combined_rect)