import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class StudentRepository():
    def __init__(self):
        self.__studentsData = []

    def addStudent(self, student):
        self.__studentsData.append(student)

    def findAllStudents(self):
        return self.__studentsData

    def findbyName(self, name):
        students = []
        for student in self.__studentsData:
            if student.getname() == name:
                students.append(student)
        return students
