class Student():
    def __init__(self, name, age, height, avgScore):
        self.__name = name  #외부에서 필드에 접근이 불가능하게 만들어야함, private : __ -> student.name 으로 접근 불가능
        self.__age = age
        self.__height = height
        self.__avgScore = avgScore

    def getName(self):  #약속 : 어떤 데이터를 가지고 오고 싶으면 get대문자단어, 직접 데이터에 접근하는 것보다 이 편이 더 안정적임
        return self.__name
    
    def getAge(slef):
        return self.__age

    def getHeight(self):
        return self.__height

    def getAvgscore(self):
        return self.__avgScore

    def setName(self, name):    # get과 반대, 외부에서 해당 객체의 데이터를 수정할 때 사용함
        self.__name = name

    def setAge(self, age):   
        self.__age = age

    def setName(self, height):    # set과 반대, 외부에서 해당 객체의 데이터를 수정할 때 사용함
        self.__height = height

    def setName(self, avgScore):    # set과 반대, 외부에서 해당 객체의 데이터를 수정할 때 사용함
        self.__avgScore = avgScore


#student.name 대신 setName/getName 을 이용해 접근함