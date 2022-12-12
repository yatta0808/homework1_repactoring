import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from view.StudentView import *
from controller.StudentController import StudentController
studentController = StudentController()
while True:
    ans = showMenu()
    if ans == '1':
        student= inputStudentInfo()
        studentController.addStudent(student)
    elif ans == '2':
        deleteStudentName = inputDeleteStudentName()
        students  = studentController.findbyName(deleteStudentName)
        showAllStudents(students)
        if inputDeleteWhether():
            studentController.deleteStudent(students)
        else:
            continue
    elif ans == '3':
        students = studentController.findAllStudents()
        showAllStudents(students)
    
    elif ans == '4':
        name = inputSearchName()
        result = studentController.searchByName(name)
        showResultHeader(name)
        showAllStudents(result)