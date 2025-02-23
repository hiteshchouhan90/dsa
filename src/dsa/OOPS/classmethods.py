"""
regular method takes first argument as the instance to take class as first 
argument use @classmethod
classmethod is  alternative constructor
staticmethod
let's give same % raise to every employee
"""


class Employee:
    raise_amt = 1.05

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        self.fname = first_name
        self.lname = last_name
        self.salary = salary

    def apply_raise(self):
        self.salary = self.salary * self.raise_amt

    @classmethod
    def set_raise_amount(cls, amount: float) -> None:
        cls.raise_amt = amount


emp1 = Employee("Hitesh", "Chouhan", 50000)
emp2 = Employee("Matt", "McEven", 60000)


emp1.apply_raise()
emp2.apply_raise()
print(emp1.fname)
print(emp1.lname)
print(emp1.salary)
print(emp2.fname)
print(emp2.lname)
print(emp2.salary)
print("-------------------")
Employee.set_raise_amount(1.20)
emp1.apply_raise()
emp2.apply_raise()
print("-------------------")
print(emp1.fname)
print(emp1.lname)
print(emp1.salary)
print(emp2.fname)
print(emp2.lname)
print(emp2.salary)
