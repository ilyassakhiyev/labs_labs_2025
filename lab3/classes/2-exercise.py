class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
print("Shape area:", shape.area())
a = int(input("Enter the side length of the square: "))
square = Square(a)
print("Square area:", square.area())
