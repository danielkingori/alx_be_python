class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return "woof!!.."

#object creation
dog1 = Dog("Buddy","Golden retriever")
dog2 = Dog("Max","German")

#accessing object properties and methods

print(f"{dog1.name} is a {dog1.breed}. He says {dog1.bark() * 3}")
print(f"{dog2.name} is a {dog2.breed}. He says {dog2.bark() * 3}")

