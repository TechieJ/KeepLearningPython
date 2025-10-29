"""
Exercise 1 — class understanding
"""
class Employee:
    company_name = "MyCompany"

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    @property
    def salary(self):
        return self.__salary

    @property
    def name(self):
        return self.__name

    @salary.setter
    def salary(self, a):
        if a < 30000 or a > 200000:
            raise ValueError("Salary should be in range of 30000 and 200000")
        else:
            self.__salary = a

    @property
    def annual_salary(self):
        return self.salary * 12

    def __str__(self):
        return f"Employee: {self.name} | Salary: {self.salary}"

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.salary + other.salary

        raise TypeError("Can only add employees object")

    def apply_raise(self, percent):
        self.salary = self.salary + (self.salary * (percent / 100))


emp1 = Employee("Alice", 60000, 28)
emp2 = Employee("Bob", 80000, 32)

print(emp1)  # Employee: Alice | Salary: 60000
print(emp1.annual_salary)  # 720000

emp1.apply_raise(10)
print(emp1.salary)  # 66000

print(emp1 + emp2)  # 146000
