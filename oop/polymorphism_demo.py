class Shape:
    def area(self):
        pass    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
            
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
            
    def area(self):
        import math
        return math.pi * (self.radius** 2)
        
# rect = Rectangle(5,12)
# print(f"The area of the rectangle is : {rect.area()}")
    
# circ = Circle(3)
# print(f"The area of a circle is: {circ.area()}")
 
    