b = "name"; # 전역변수

class MyStatus:
    def __init__(self,age,name) -> None: # -> 이후는 리턴이 어떤것이 갈것인지를 나타내는 주석임.
        self.age = age
        self.name = name
    
    def printAge(self):
        print(self.age)
        print(b)

    def printName(self):
        return self.name
    

a = MyStatus(13,"주진성")

a.printAge()
print(a.printName())


class Calc:
    def __init__(self, score) -> None: # 정수값 리턴
        self.score = score # 인스턴스 변수 정의
    
    def calcScore(self):
        realScore = self.score

        match realScore :
            case realScore if realScore > 0 and realScore < 10:
                return "F"
            
            case realScore if realScore > 11 and realScore < 20 :
                return "E"
            
            case _:
                return "null"
            
    def test(self):
        return self.score

b = Calc(13)
print(b.calcScore())
print(b.test())

