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
    if ans == '3':
        students = studentController.findAllStudents()
        showAllStudents(students)