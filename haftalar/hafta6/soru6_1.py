class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def to_string(self):
        return f'name: \"{self.name}\" salary: {self.__salary}'
    def get_salary(self):
        return self.__salary
    def set_salary(self, new_salary):
        self.__salary = new_salary

emp1 = Employee('Ali', 1234)
print(emp1.to_string())

emp1.set_salary(555)
print(emp1.to_string())

print(emp1._Employee__salary)
