class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        pass
    
#inheritance
class Lion(Animal):
    def speak(self):
        return f"{self.name} the lion roars"
    
class Elephant(Animal):
    def speak(self):
        return f"{self.name} the Elephant triumphs"
    
#polymorphism
zoo = [
    Lion("Simba"),
    Elephant("Dumbo")
]

for animal in zoo:
    print(animal.speak())