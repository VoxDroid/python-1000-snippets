# sample1.py
# Employee salary property example from README

class Employee:
    def __init__(self, name, salary):
        self._salary = salary
        self.name = name
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

if __name__ == '__main__':
    emp = Employee('Bob', 50000)
    print('Salary:', emp.salary)
    emp.salary = 60000
    print('Updated Salary:', emp.salary)
