class student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_marks(self):
       return self.__marks
    def set_marks(self,marks):
       self.__marks=marks

s=student("yash",50)

print("Name:",s.name)
print("Marks:",s.get_marks)
s.set_marks(20)
print(" Updated Marks:",s.get_marks)