class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def compute_area(self):
        area = self.length * self.width
        print(area)

rectangle_instance = Rectangle(3, 4)
rectangle_instance.compute_area()

