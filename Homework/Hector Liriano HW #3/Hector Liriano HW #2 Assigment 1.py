# 7/7

class Person:

    def __init__(self, name, height, age, ethnicity):
        self.name = name
        self.height = height
        self.age = age
        self.ethnicity = ethnicity

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Student(Person):

    def __init__(self, name, height, age, ethnicity, gpa, major):

        Person.__init__(self, name, height, age, ethnicity)
        self.gpa = float(gpa)
        self.major = major

    def getGPA(self):
        return self.gpa

    def getMajor(self):
        return self.major

    def UpdateAge(self):
        self.age = self.age + 1

    def setGPA(self, gpa):
        self.gpa = float(gpa)

class CUNY_Student(Student):

    def __init__(self, name, height, age, ethnicity, gpa, major, graduationYear):

        Student.__init__(self, name, height, age, ethnicity, gpa, major)
        self.graduation = graduationYear

    def getGraduation(self):
        return self.graduation

    def UpdateAge(self):
        self.age = self.age - 1
