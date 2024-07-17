#magic methods - dunder methods, special methods with double underscores for defining specific behaviours
#constructor (__init__)--> initializes objects attributes
#destructor (__del__) clean up tasks before object destruction

#self - variable that refers to current instance
class Point:
    count = 0
    #called when we create an object
    def __init__(self, value_one, value_two): #PEP - coding conventions
        self.x = value_one
        self.y = value_two
        
    # def __str__(self):
    #     return f"( x={self.x}, y={self.y} )"
    
    # def __del__(self):
    #     print(f"Object {self} has been destroyed")
    
    #research
    #def __
    
    #instance method , instance attributes
    def hello(self):
        pass

    @classmethod
    def hello2(cls):
        print(f"The value of cls is {cls}")
    
#creating objects/occurence/instance of a class 
# point1 = Point(1,1)
# point2 = Point(3,2.5)

# print(point2)
# del point2
# print(point2)



#class methods - works with class attributes - work with class methods like count

#@class method decorator, turns our class into a class method

class MyClass:
    class_variable = 'class variable'

    @classmethod
    def class_method(cls):
        print(f'Called class_method of {cls}')
        print(cls.class_variable)

MyClass.class_method()  # This is how you call a class method
obj = MyClass()
obj.class_method()  # This also works


class MyClass:
    def instance_method(self):
        print(f'Called instance_method of {self}')

obj = MyClass()
obj.instance_method()  # This is how you call an instance method
