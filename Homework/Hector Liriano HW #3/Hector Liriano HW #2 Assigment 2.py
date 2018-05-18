# 6/7
# On UMLs: 5/6
# Inheritance arrow is one-directional, from child to parent.
# Arrow from Professor to Course is an "association" so
# arrow should not be triangle, but other arrow.

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

class Professor(Person):

    def __init__(self, name, height, age, ethnicity):

        Person.__init__(self, name, height, age, ethnicity)
        self.Course = Course()
        self.courses = {}
        self.period = 1

    def addCourse(self,name):
            
        self.courses[self.period] = [name,self.Course.setCourseLocation(),
                              self.Course.setCourseDate(),
                              self.Course.setCourseTime()]

        if self.Course.isCourseConflict(self.courses, self.period) == True:
            self.courses.pop(self.period)
            
        else:
            self.period = self.period + 1

    def getCourse(self):

        for course in range(len(self.courses)):

            print("Class: " + self.courses[course+1][0] +
                  "\nLocation: " + self.courses[course+1][1] +
                  "\nDay: " + self.courses[course+1][2] +
                  "\nTime: " + self.courses[course+1][3] + "\n")
                  

class Course:

    def __init__(self):
        self.location = ""
        self.date = ""
        self.time = ""
    
    def setCourseLocation(self):
        self.location = str(input("Where is it? "))

        return self.location
        
    def setCourseDate(self):
        self.date = str(input("What day? "))

        return self.date

    def setCourseTime(self):
        self.time = str(input("What time? (Ex: 2-4pm): "))

        return self.time

    # COMMENT: Wow, I was asking for simpler scenario than this!
    # Not clear what Course and period are?
    # Notice below that you are repeating code for dealing with "am" and "pm"
    # Better to make into one function that does both parts.
    def isCourseConflict(self, Course, period):

        if len(Course) > 1:

            if "am" in Course[period][3]:

                tempvar = Course[period][3].split("am")
                newClassStartTime = int("".join(tempvar).split("-")[0])
                newClassEndTime = int("".join(tempvar).split("-")[1])
                
            else:
                tempvar = Course[period][3].split("pm")

                if len("".join(tempvar).split("-")[0]) == 1 and \
                   len("".join(tempvar).split("-")[1]) == 2 and \
                   int("".join(tempvar).split("-")[1]) != 12:

                    newClassStartTime = 12 + int("".join(tempvar).split("-")[0])

                elif len("".join(tempvar).split("-")[0]) == 1 and \
                   len("".join(tempvar).split("-")[1]) == 1:

                    newClassStartTime = 12 + int("".join(tempvar).split("-")[0])
                    newClassEndTime = 12 + int("".join(tempvar).split("-")[1])

                else:
                    newClassStartTime = int("".join(tempvar).split("-")[0])
                    newClassEndTime = 12 + int("".join(tempvar).split("-")[1])

            
            for p in range(period):

                if Course[period][2] == Course[p+1][2] and period != p+1:

                    if "am" in Course[p+1][3]:

                        tempvar = Course[p+1][3].split("am")
                        otherClassStartTime = int("".join(tempvar).split("-")[0])
                        otherClassEndTime = int("".join(tempvar).split("-")[1])
                        
                    else:
                        tempvar = Course[p+1][3].split("pm")

                        if len("".join(tempvar).split("-")[0]) == 1 and \
                           len("".join(tempvar).split("-")[1]) == 2 and \
                           int("".join(tempvar).split("-")[1]) == 12:

                            newClassStartTime = 12 + int("".join(tempvar).split("-")[0])
                            otherClassEndTime = int("".join(tempvar).split("-")[1])

                        elif len("".join(tempvar).split("-")[0]) == 1 and \
                           len("".join(tempvar).split("-")[1]) == 1:

                            otherClassStartTime = 12 + int("".join(tempvar).split("-")[0])
                            otherClassEndTime = 12 + int("".join(tempvar).split("-")[1])

                        elif len("".join(tempvar).split("-")[0]) == 2 and \
                           len("".join(tempvar).split("-")[1]) == 2 and \
                           int("".join(tempvar).split("-")[1]) == 12:

                            otherClassStartTime = int("".join(tempvar).split("-")[0])
                            otherClassEndTime = int("".join(tempvar).split("-")[1])

                    # COMMENT: Some problem with logic below.
                    # Should start at otherClassStartTime, not otherClassStartTime + 1
                    # And if newClassStartTime == otherClassEndTime that should be ok.
                    if newClassStartTime in range(otherClassStartTime + 1,  
                                                  otherClassEndTime + 1) or \
                        newClassEndTime in range(otherClassStartTime + 1,
                                                  otherClassEndTime + 1):

                        print("\nCourse conflicts with " + str(Course[p+1][0]))

                        return True

