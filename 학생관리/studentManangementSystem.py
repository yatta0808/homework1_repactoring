import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from view.StudentView import *
from controller.StudentController import StudentController
studentController = StudentController()
while True:
    ans = showMenu()
    if ans == '1':
        student= inputStudentAllInfo()
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
        name = inputName("search")
        result = studentController.searchByName(name)
        showResultHeader(name)
        showAllStudents(result)


    elif ans == '5':
        break
    
    elif ans == '6':
        name = inputName("update")
        if studentController.presenceOrAbsence(name):
            updateData = inputStudentInfoWithoutName(name)
            studentController.updateStudent(updateData)
        else:
            showNone()

    elif ans == '7':
        top3 = studentController.searchTopScoreStudent()
        showTop3Students(top3)
