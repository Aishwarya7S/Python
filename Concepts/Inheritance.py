class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Makes sound")

class Cat(Animal):
    def sound(self):
        print(f"Cat name: {self.name} ")

c = Cat("Rishi")
c.sound()
