import math
class circle:
    def __init__(self):
        self.radius=float(input("enter the radius :"))
        self.get_area()
    def get_area(self):
        return (self.radius**2)*math.pi
circle1=circle()
print(round(circle1.get_area(),2))

