MENU_MESSAGE = "메뉴를 선택하세요 : "

def showMenu():
    print("----[학생 관리 프로그램]----\n","1. 학생 추가\n","2. 학생 삭제\n","3. 학생 전체 조회\n","4. 학생 검색\n", "5. 종료", end = "\n")
    return input(MENU_MESSAGE)
    
def inputStudentInfo():
    name = input("학생의 이름을 입력하세요 : ")
    age = int(input("학생의 나이를 입력하세요: "))
    height = int(input("학생의 키를 입력하세요 :"))
    avgScore = int(input("학생의 평균 점수를 입력하세요 :"))
    return [name, age, height, avgScore]


def showAllStudents(students):
    print("----등록되어 있는 학생 목록----")
    for student in students:
        print(f"이름: {student[0]}, 나이 : {student[1]}, 키 : {student[2]}, 평균 점수 : {student[3]}")

def inputDeleteStudentName():
    return input("삭제할 학생의 이름을 입력하세요: ")

def inputDeleteWhether():
    ans = input("해당 학생이 맞습니까? (y/n) : ")
    if ans == "y":
        return True
    elif ans == "n":
        return False 

def inputSearchName():
    return input("검색할 단어를 선택하세요: ")

def showResultHeader(name):
    print(f'---- \"{name}\"로 검색한 결과입니다. ----')