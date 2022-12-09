import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from repos.StudentRepository import StudentRepository
from service.StudentService import *

class StudentController():
    
    def __init__(self): #controller는 repos를 호출하므로 가지고 있어야 함

        self.studentRepository = StudentRepository()

    def addStudent(self,student):
        self.studentRepository.addStudent(changeListToObject(student))
        
    def findAllStudents(self):
        return changeAllObjectToList(self.studentRepository.findAllStudents())

    def findbyName(self, name):
        return self.studentRepository.findbyName()
