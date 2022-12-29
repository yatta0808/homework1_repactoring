import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from domain.Student import Student
class StudentRepository():

    def __init__(self):
        studentDataBase = open("./repos/students.txt","r", encoding='UTF8')
        self.__studentsData = []
        lines = studentDataBase.readlines()
        for line in lines:
            info = line.split(',')
            info[3] = info[3].rstrip()
            readStudent = Student(info[0], info[1], info[2], info[3])
            self.__studentsData.append(readStudent)
        studentDataBase.close()

    def addStudent(self, student):
        studentDataBase = open("./repos/students.txt","a", encoding='UTF8')
        data = student.toString()
        studentDataBase.write(data)
        self.__studentsData.append(student)
        studentDataBase.close()

    def findAllStudents(self):
        return self.__studentsData

    def findByName(self, name):
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


    def updateStudent(self, updateData):
        updateStudentName = updateData.getName()
        for student in self.__studentsData:
            if student.getName() == updateStudentName:
                student.setAge(updateData.getAge())
                student.setHeight(updateData.getHeight())
                student.setAvgScore(updateData.getAvgScore())

    def searchTopScoreStudent(self):
        sortedAvgScores = []
        top3 = []
        for student in self.__studentsData:
            sortedAvgScores.append(student.getAvgScore())
        sortedAvgScores.sort(reverse=True)
        print(sortedAvgScores)
        for i in range(0,3):
            for student in self.__studentsData:
                if student.getAvgScore() == sortedAvgScores[i] and student not in top3:
                    top3.append(student)
                    break
        return top3

    