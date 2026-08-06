class school:
    def type(self):
        print("Schoool")
class student:
    def __init__(self,) -> None:
        self.school = school()

    def learn(self):
        self.school.type()
        print("student learns in school")


student1=student()
student1.learn()

