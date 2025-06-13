# Eg 1
class Student:
    def show(self):
        print("I'm a Student")

stu = Student()
stu.show()

# Eg 2
class Student:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Aishu", 20)  
s1.show()
