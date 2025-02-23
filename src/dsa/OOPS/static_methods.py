import datetime

"""static methods are when you don't access the instance and the logic has 
    something to do witht the class
"""


class Employee:
    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        self.fname = first_name
        self.lname = last_name
        self.salary = salary

    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


day = datetime.date(2016, 12, 15)
print(Employee.is_weekday(day))
