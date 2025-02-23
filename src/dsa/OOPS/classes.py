class Employee:
    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        self.fname = first_name
        self.lname = last_name
        self.salary = salary

    def salary_after_raise(self, raise_percent: float) -> None:
        self.salary = self.salary * raise_percent


emp1 = Employee("Hitesh", "Chouhan", 50000)
emp2 = Employee("Matt", "McEven", 60000)

print(emp1.fname)
print(emp1.lname)
print(emp1.salary)
print(emp2.fname)
print(emp2.lname)
print(emp2.salary)
print("-------------------")
print(emp1.salary_after_raise(1.40))
print(emp2.salary_after_raise(1.10))
print("-------------------")
print(emp1.fname)
print(emp1.lname)
print(emp1.salary)
print(emp2.fname)
print(emp2.lname)
print(emp2.salary)
