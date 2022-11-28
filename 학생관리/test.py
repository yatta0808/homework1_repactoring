import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from controller.StudentController import StudentController
from domain.Student import Student

studentController = StudentController()
cs = Student("철수",14,140,50)

studentController.addStudent(cs)

print(studentController.showAllStudent())