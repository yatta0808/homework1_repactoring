import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from repos.StudentRepository import StudentRepository

class StudentController():
    
    def __init__(self): #controller는 repos를 호출하므로 가지고 있어야 함

        self.studentRepository = StudentRepository()

    def addStudent(self,student):
        self.studentRepository.addStudent(student)

    def showAllStudent(self):
        return self.studentRepository.findAllStudents()