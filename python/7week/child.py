from person import Person

class Student(Person):
    def __init__(self, fname, lname, course):
        super().__init__(fname, lname)
        self.course = course
        self.graduationyear = 2024
    def printname(self):
        print(self.firstname, self.lastname, self.course)
x = Student("Mike", "Olsen", 3)

x.printname()