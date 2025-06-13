class Employee:
    def __init__(self, name, dept, salary):
        self.name = name           # Public
        self._dept = dept          # Protected
        self.__salary = salary     # Private

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 10000:
            self.__salary = salary
        else:
            print("Salary must be more than 10000!")

    def show_info(self):
        return f"Name: {self.name}, Dept: {self._dept}, Salary: {self.__salary}"

emp = Employee("Aishaa", "CSE", 25000)
print(emp.name)           # Public
print(emp._dept)          # Protected
print(emp.get_salary())   # Private via getter

emp.set_salary(30000)
print(emp.show_info())
