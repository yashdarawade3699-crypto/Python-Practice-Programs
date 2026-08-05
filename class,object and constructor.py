class student:
    def __init__(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch

    def display(self):
        print("Student details:")
        print ("Name:",self.name)
        print ("Age:",self.age)
        print ("Branch:",self.branch)



student1=student("Yash",22,"CSE")
student1.display()
student2=student("Sam",21,"CSE + mechanical")
student2.display()
        
