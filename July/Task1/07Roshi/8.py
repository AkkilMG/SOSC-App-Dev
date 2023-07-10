class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Overloading
def calc_area(shape):
    if isinstance(shape, Shape):
        return shape.area()
    else:
        raise TypeError("Invalid shape type")

# Overriding
def calc_area(shape):
    if isinstance(shape, Rectangle):
        return shape.area()
    elif isinstance(shape, Circle):
        return shape.area()
    else:
        raise TypeError("Invalid shape type")

rectangle = Rectangle(5, 3)
circle = Circle(4)

print("Area of Rectangle is",calc_area(rectangle))  
print("Area of Circle is",calc_area(circle))    


"""OutPut:
Area of Rectangle is 15
Area of Circle is 50.24  """