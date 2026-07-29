class Employee:

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary


    @property
    def salary(self)->float:
        return self._salary

    @salary.setter
    def salary(self, value:float):
        if value<0:
            raise ValueError("Salary cannot be negative!")
        self._salary = value

emp1 = Employee("bk", 10000)
print(emp1.salary)
print(Employee.__dict__)
