def greet(func):
    def wrapper(self):
        print("Employee Information")
        func(self)
        print("End of Record")
    return wrapper

class Employee:
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary

    @greet
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

e1 = Employee("Rahul", 50000)
e1.display()