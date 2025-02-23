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

    @classmethod
    def from_string(cls, emp_str: str):
        fname, lname, salary = emp_str.split("-")
        return cls(fname, lname, salary)


emp1 = "Hitesh-Chouhan-50000"
emp2 = "Matt-McEven-60000"

emp_obj1 = Employee.from_string(emp1)
emp_obj2 = Employee.from_string(emp2)

print(emp_obj1.fname)
print(emp_obj2.fname)
