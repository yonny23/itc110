from grade import Grade

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
        gradeList=self.student.getGrades
        for i in range(len(gradeList)):
            print(gradeList[i].course, gradeList[i].credits, gradeList[i].score)
        gpa = self.student.calculateGPA()
        print ("The GPA is ", gpa)
        
def main():
    display=Display()
main()
