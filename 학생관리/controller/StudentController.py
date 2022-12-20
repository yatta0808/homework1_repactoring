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
        students  = self.studentRepository.findbyName(name)
        students = changeAllObjectToList(students)
        return students

    def deleteStudent(self, students):
        #학생은 1 명일 수도 있고 여러 명일 수도 있지만
        #지금 당장은 1 명으로 가정하고
        #나중에 기능 추가한다.
        student = students[0]
        student = changeListToObject(student)
        self.studentRepository.deleteStudent(student)

    def searchByName(self, name):
        searchResult = self.studentRepository.searchByName(name)
        return changeAllObjectToList(searchResult)

    def updateStudent(self,updateData):
        self.studentRepository.updateStudent(changeListToObject(updateData))

    def presenceOrAbsence(self, name):
        return presenceOrAbsenceService(self.studentRepository.findByName(name))
        