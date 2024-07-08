class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def info(self):
        return f"this is:"
        
std1 = Student("Kamau","10")
std2 = Student("john","8")

print(f"{std1.info()}{std1.name} , he is {std1.age} years old")