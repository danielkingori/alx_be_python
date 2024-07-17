#magic methods - dunder methods, special methods with double underscores for defining specific behaviours
#constructor (__init__)--> initializes objects attributes
#destructor (__del__) clean up tasks before object destruction

#self - variable that refers to current instance
class Point:
    #called when we create an object
    def __init__(self, value_one, value_two): #PEP - coding conventions
        self.x = value_one
        self.y = value_two
        
    def __str__(self):
        return f"( x={self.x}, y={self.y} )"
    
    def __del__(self):
        print(f"Object {self} has been destroyed")
    
    #research
    #def __
#creating objects/occurence/instance of a class 
point1 = Point(1,1)
point2 = Point(3,2.5)

print(point2)
del point2
print(point2)

#instance method , instance attributes
def hello(self):
    pass

@classmethod
def hello2(cls):
    print(f"The value of cls is {cls}")

#class methods - works with class attributes - work with class methods like count

#@class method decorator, turns our class into a class method