class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, x_offset, y_offset):
        new_x = self.x + x_offset
        new_y = self.y + y_offset
        print(new_x, new_y)

    def dist(self, x_target, y_target):
        dist_x = x_target - self.x
        dist_y = y_target - self.y
        print((dist_x**2 + dist_y**2)**0.5)


p1 = Point(5, 3)
p1.show()
p1.move(3, 3)
p1.dist(8, 7)
