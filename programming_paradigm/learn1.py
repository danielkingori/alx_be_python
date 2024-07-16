#encapsulation - a principle in OOP that allows methods and attributes to be infused/bundled inside a class
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


#inheritance - principle in OOP that allows for class or subclass that inherits methods and attributes from existing super class

#object is an instance of a class
class Student(Person):
    def __init__(self, name, age, student_id):
        #super - special function used to inherit from a super/base class 
        #gives you access to the parent class
        super().__init__(name, age)
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = []
        
    def enrol(self, course):
        self.course.append(course)
        return f"{self.name} enrolled in {self.course}"
    
    
    def __str__(self):
        return f"{self.name}, {self.age}, {self.student_id}, {self.walk()}"
        
Student1 = Student("henry", 40, 2)
print(Student1)
#print(Student1.walk())
print(Student1.enrol("Maths"))

