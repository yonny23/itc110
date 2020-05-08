class Grade():
    def __init__(self, course, credits, score):
        self.course=course
        self.credits=credits
        self.score=score

    def getCourse(self):
        return self.course

    def getCredits(self):
        return self.credits

    def getScore(self):
        return self.score

class Student():
    def __init__ (self, SID, name, email):
        self.SID=SID
        self.name=name
        self.email=email
        self.grades=[]


    def getSID(self):
        return self.SID

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def addGrade(self,grade):
        self.grades.append(grade)
    
    def getGrades(self, grades):
        return self.grades

    def calculateGPA(self):
        totalCredits=0.0
        totalWeight=0.0
        gpa=0.0
        if len(self.grades) !=0:
            for i in range(len(self.grades)):
                totalCredits += self.grades[i].credits
                totalWeight += self.grades[i].credits * self.grades[i].score
            gpa = totalWeight / totalCredits
        return gpa

    def __str__(self):
        return self.SID + " " + self.name + " " + self.email


class Display():

    def __init__(self):
        self.makeStudent()
        self.enterGrades()
        self.outputStuff()
        
    def makeStudent(self):
        sid = input("Enter the Student SID ")
        name = input("Enter the student name ")
        email = input("Enter the student email ")
        self.student = Student(sid,name,email)
    
    def enterGrades(self):
       done='n'
       while done == 'n':
           course=input("Enter the course name ")
           credits=float(input("Enter the number of credits "))
           finalGrade=float(input("Enter the final grade "))
           self.grade = Grade(course, credits, finalGrade)
           self.student.addGrade(self.grade)
           done = input("Done n/y to quit ")
           done=done.lower()

    def outputStuff(self):
        print(self.student)
        gradeList=self.student.getGrades()
        for i in range(len(gradeList)):
            print(gradeList[i].course, gradeList[i].credits, gradeList[i].score)
        gpa = self.student.calculateGPA()
        print ("The GPA is ", gpa)
        
def main():
    display=Display()
main()

