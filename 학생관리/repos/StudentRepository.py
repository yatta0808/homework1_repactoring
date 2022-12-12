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
            if student.getName() == name:
                students.append(student)
        return students

    def deleteStudent(self, student):
        for s in self.__studentsData:
            if student.getName() == s.getName():
                del self.__studentsData[self.__studentsData.index(s)]
                break

    def searchByName(self, name):
        searchResult = []
        for student in self.__studentsData:
            if name in student.getName():
                searchResult.append(student)
        return searchResult