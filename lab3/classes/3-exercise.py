class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

b = int(input("Enter the length of the rectangle: "))
c = int(input("Enter the width of the rectangle: "))
rect = Rectangle(b, c)
print("Rectangle area: ", rect.area())