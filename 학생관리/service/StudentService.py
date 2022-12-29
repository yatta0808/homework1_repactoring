import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from domain.Student import Student

def changeListToObject(enteredStudent):
    student = Student(enteredStudent[0], enteredStudent[1], enteredStudent[2], enteredStudent[3])
    return student

def changeObjectToList(enteredStudent):
    student = [enteredStudent.getName(),
    enteredStudent.getAge(),
    enteredStudent.getHeight(),
    enteredStudent.getAvgScore()]

    return student

def changeAllObjectToList(enteredStudents):
    students = []
    for enteredStudent in enteredStudents:
        students.append(changeObjectToList(enteredStudent))
    return students

def presenceOrAbsenceService(students):
    if len(students) > 0:
            return True
    else:
            return False

def findTopScoreStudent(students):
    studentDic = {}
    for student in students:
        studentDic[student.getName()] = int(student.getAvgScore())
    sorted_studentDic = sorted(studentDic.items(), key = lambda item: item[1], reverse=True)
    return sorted_studentDic[0:3]