class Employee:
    def __init__(self,first_name :str, last_name: str, salary :float) -> None:
        self.fname = first_name
        self.lname = last_name
        self.email = first_name + last_name + '@company.com'
        self.salary = salary

class Developer(Employee):
    def __init__(self, first_name: str, last_name: str, salary: float, prog_lang :str) -> None:
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first_name :str, last_name: str, salary :float, dev: Developer) -> None:
        super().__init__(first_name, last_name, salary,)
        if not isinstance(dev, Developer):
            raise TypeError("Expected type of dev is an object of Developer class")
        
decorator
pydantic base models
