class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


rectangle = Rectangle(4, 5)
circle = Circle(3)

print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

print("\nCircle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

# OUTPUT
# Rectangle Area: 20
# Rectangle Perimeter: 18

# Circle Area: 28.259999999999998
# Circle Perimeter: 18.84
