# OOPs 
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.__roll = roll
        self.marks = marks

    def display(self):
        print(f"Name: {self.name} \nRoll Number: {self.__roll} \nMarks: {self.marks}")

    def get_roll(self):
        return self.__roll
    
    def calculateGrade(self):
        if self.marks >= 90:
            return 'O'
        elif self.marks >= 80:
            return 'A'
        elif self.marks >= 70:
            return 'B'
        elif self.marks >= 60:
            return 'c'
        else:
            return 'D'
        
class Topper(Student):
    def __init__(self, name, roll, marks,award):
        super().__init__(name, roll, marks)
        self.award = award
        
    def show(self):
        print("Award: ", self.award)
        

stu = Student("Rishi", 3, 73)
stu.display()
print("Grade: ", stu.calculateGrade())
print()

topstu = Topper("Atharvaa", 7, 97, "Best Student")
topstu.display()
print("Grade: ", topstu.calculateGrade())
topstu.show()
