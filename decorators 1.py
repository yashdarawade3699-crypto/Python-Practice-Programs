def info(func):
    def wrapper(self):
        print("Student Details:")
        func(self)
        print("Record Displayed Successfully")
    return wrapper

class Student:
    def _init_(self, name, roll):
        self.name = name
        self.roll = roll

    @info
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)

s1 = Student("Yash", 101)
s1.display()