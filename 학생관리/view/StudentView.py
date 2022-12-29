MENU_MESSAGE = "메뉴를 선택하세요 : "
SEARCH_INPUT_MESSAGE = "검색할 단어를 선택하세요: "
UPDATE_INPUT_MESSAGE = "수정할 학생의 이름을 입력하세요: "

def showMenu():
    print("----[학생 관리 프로그램]----\n","1. 학생 추가\n","2. 학생 삭제\n","3. 학생 전체 조회\n","4. 학생 검색\n", "5. 종료\n", "6. 학생 정보 수정\n","7. 점수 순위 확인",end = "\n")
    return input(MENU_MESSAGE)
    
def inputStudentAllInfo():
    name = inputStudentNameInfo()
    age = inputStudentAgeInfo()
    height = inputStudentHeightInfo()
    avgScore = inputStudentAvgScoreInfo()
    return [name, age, height, avgScore]

def inputStudentNameInfo():
    return input("학생의 이름을 입력하세요 : ")

def inputStudentAgeInfo():
    return int(input("학생의 나이를 입력하세요 : "))

def inputStudentHeightInfo():
    return int(input("학생의 키를 입력하세요 : "))

def inputStudentAvgScoreInfo():
    return int(input("학생의 평균 점수를 입력하세요 : "))

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

def inputName(type):
    if type == "search":
        return input(SEARCH_INPUT_MESSAGE)
    elif type == "update":
        return input(UPDATE_INPUT_MESSAGE)

def showResultHeader(name):
    print(f'---- \"{name}\"로 검색한 결과입니다. ----')

def showNone():
    print("해당 학생이 존재하지 않습니다.")

def inputStudentInfoWithoutName(updatedname):
    name = updatedname
    age = inputStudentAgeInfo()
    height = inputStudentHeightInfo()
    avgScore = inputStudentAvgScoreInfo()
    return [name, age, height, avgScore]

def showTop3Students(students):
    for i in range(1, len(students)+1):
        print(i, "등 : ",students[i-1])