#encapsulation - a principle in OOP that allows methods and attributes to be infused /bundled inside a class
class Person:
    #instantiate the class and add properties using the init method
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #function within a class is a method
    def walk(self):
        return f"I can wlak"
    #use str to access the attributes/properties
    def __str__(self):
        return f"{self.name} {self.age}"
    
person1 = Person("jon", 30)
print(person1.walk())
print(person1)