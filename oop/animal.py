class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        pass
    
#inheritance
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)