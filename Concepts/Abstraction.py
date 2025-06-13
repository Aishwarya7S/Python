from abc import ABC, abstractmethod

class Employee(ABC):                        # abstract class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):             # abstract method
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 70000

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 30000

emp1 = FullTimeEmployee("Aishu")
emp2 = PartTimeEmployee("Rishi")

print(emp1.name, "Salary:", emp1.calculate_salary())
print(emp2.name, "Salary:", emp2.calculate_salary())
