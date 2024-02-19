# class , 함수 , 인스턴스 , __init__
- [관련해서 잘 정리되어잇는 블로그, 여기는 함축해서 써놧음](https://engineer-mole.tistory.com/190)

## def , 함수
python에서 함수, 메서드를 정의하기 위해서는 `def` 키워드를 사용함.

class 내부에서도 사용할 수 있고, 외부에서도 사용이 가능함.
- class 내부에서 생성된 함수는 메서드

```python
class SomeClass:
    def __init__(self,something):
        self.something = something

    def some_function(self):
        print(self.something)
```

## class와 __init__
Python에서 class는 다음과 같이 정의할 수 있음.

```python
class MyStatus:
    pass
```

또한 class는 `__init__` 메서드를 가지고 있음.

`__init__` 메서드는 class가 호출될 때 처음 호출되는 함수임.
- 초기화 함수
- 컨스트럭터라고 불리는 초기화를 위한 함수(메소드)
- 인스턴스화를 실시할 때 반드시 처음에 호출되는 특수한 함수
- 오브젝트 생성(인스턴스를 생성)과 관련하여 데이터의 초기를 실시하는 함수

또한 `__init__` 메서드는 파라미터로 꼭 self 를 가져야만 하는데, 이는 클래스가 처음 생성될 때 파라미터를 클래스 내부에서 사용하기 위해 초기화하는것으로 보면 됨.

```python
class MyStatus:
    def __init__(self,age,name) -> None: # -> 이후는 리턴이 어떤것이 갈것인지를 나타내는 주석임.
        self.age = age
        self.name = name
    ...
```

## 인스턴스 
class를 선언할 때 , 파라미터로 받은 변수를 의미함.

class 내부의 메서드에서 사용하기 위해선, `self.변수명` 형태로 호출하여 재 정의한뒤 사용하면 됨.

클래스를 선언할 때 인스턴스 변수를 직접 선언하는 것이 아니라, `__init__` 메서드(또는 다른 메서드) 내에서 self.변수명 형태로 인스턴스 변수를 초기화하고 정의함. 

이렇게 정의된 인스턴스 변수는 클래스의 다른 메서드에서 self.변수명을 통해 접근할 수 있음.

```python
class cal:
    def __init__(self,myscore) -> None:
        self.myscore = int(myscore)

    def calScore(self):
        realScore = self.myscore # 인스턴스 변수 재 정의

        match realScore :
            case realScore if realScore > 0 and realScore < 10:
                return "F"
            
            case realScore if realScore > 11 and realScore < 20 :
                return "E"
            
            case _:
                return "null"
```

생성한 class를 사용하기 위해서 "인스턴스" 를 생성해야 함.

인스턴스란 클래스를 실채화한 것임. 

```python
class SomeClass:
    def __init__(self,something):
        self.something = something

    def some_function(self):
        print(self.something)
        
a = SomeClass("some_value")
a.some_function()
#함수에서 print 내장함수를 사용하고 있으므로 some_value가 리턴된다.
```