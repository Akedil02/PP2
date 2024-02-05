class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

# Example of using the classes
shape = Shape()
print("Area of Shape:", shape.area())

square = Square(4)  # Creating a square with length 4
print("Area of Square:", square.area())
