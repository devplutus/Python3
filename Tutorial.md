# Data Type
## String

    String1 = 'string1'
    String2 = "string2"
    StringFormat = "{} + {}"
    StringFormat.format(String1, String2) # strgin1 + string2
    String3 = """ " and ' """ # " and '


## Number

    num1 = 3 # int
    num2 = 3.0 # float
    num3 = 4 / 4 # 1.0(float)
    num4 = 4 // 4 # 1(int)
    num5 = 12 % 5 # 2(int)

    num1 = float(num1) # 3.0(float)
    num2 = int(num2) # 3(int)
    
    
## Bool

    bool(0) # False
    bool(-1) # True
    bool(None) # False
    bool([]) # False
    bool('') # False
    bool('A') # True

## Type 확인

    type(a) # type(변수명) : 자료형 반환
    isinstance(42, int) # isinstance(값, 자료형) : 자료형 검사
    

# Data Structures
## List

    list1 = [0, 1, 2, 3, 4, 5] # size = 6
    list1[-1] # 5(뒤에서 첫번째)
    list1[-7] # Excpetion : out of range

    list2 = 6
    list1 = list1 + list2 # == list1.append(6) ([0, 1, 2, 3, 4, 5, 6])
    del list1[-1] # == del(list[-1]) == list1.remove(6) ([0, 1, 2, 3, 4, 5])

    find = 3

    if find in list1: # list1 안에 3이 있는지 확인.
      print("Exist")

#### list.append(value) : value를 맨 뒤에 추가
#### list.pop(index) : list의 index 값을 삭제
#### list.index(value) : value를 가진 index를 반환
#### list.extend([value1, valu2...]) : 리스트 뒤에 리스틀 추가
#### list.insert(index, value) : list의 index에 value를 추가
#### list.sort() : 값을 순서대로 정렬(Default : ASC)
#### list.reverse() : 값을 역순으로 정렬
#### List Slice
    """
    slice를 하면 해당하는 부분의 리스트나 문자열을 **새로 만들어** 준다.
    list[start:end:step=1]
    """
    text = "01234567"
    text[1:5] # 1 <= idx and idx < 5
    text[1:] # 1<= idx
    text[:5] # idx < 5
    text[:] # all
    step=2
    text[::step] # [0,2,4,6]
    text[len(text)::-1] # [7,6,5,4,3,2,1,0]
    del text[:2] # [2,3,4,5,6,7]
    text[:2] = [8, 9] # [8,9,4,5,6,7]
    text[:2] = [8, 9, 10] # [8,9,10,4,5,6,7]
    text[:2] = [8] # [8,10,4,5,6,7]

#### List와 String
    """
    맨 처음 C를 공부하면 String이 Char형의 배열인것을 알 수 있다.
    """
    str1 = "ABCD"
    
    for c in str1:
        print(c) # A B C D
    print(str1[0]) # A
    
    list1 = list(str1) # ['A', 'B', 'C', 'D']
    list2 = str1.split() # ['A', 'B', 'C', 'D']
    
    str2 = "16:24:30"
    list3 = str2.split(":")
    print(list3) # ['16', '24', '30']
    
    str3 = ":".join(list3)
    print(str3) # "16:24:30"
    
    
    
    
    
  

## Dictionary
* for문을 사용하면 key는 순서대로 나오지 않는다.

        dic = {
          "A" : 1,
          "B" : 2,
          "C" : 3
        }

        for key in dic.keys(): # or for key in dic:
            print(key) # A B C

        for value in dic.values():
            print(value) # 1 2 3

        for k, v in dic.items():
            print("{} {}".format(k, v), end = " ") # A 1 B 2 C 3
  
  
## Dictionary 와 List 차이점
* 합치기

        list1 = [0, 1, 2, 3]
        list2 = list + [4, 5, 6]
        
        dic1 = {'one':1, 'two', 2}
        dic2 = {'three':3, 'four',4}
        di1.update(dic2)
* 찾기

        1 in list1
        'one' in dic1.keys()
        2 in dic1.values()



## Tuple
* List와 다르게 추가, 삭제, 변경이 불가능하다.

        tuple1 = (1, 2, 3)
        tuple2 = 1, 2, 3 # 괄호 생략가능
        list1 = [1, 2, 3]
        tuple3 = tuple(list1) # Tuple Type으로 변경 가능하다.

* packing, unpacking

        tuple1 = (1, 2)
        a, b = tuple1 # a = 1, b = 2 unpacking
        tuple2 = a, b # tuple2 = (1, 2) packing
        a, b = b, a # a = 2, b = 1



# IO
## Input

    a = input("Type") # == print("Type")
                           a = input()

## Print
    a = 1
    b = 2
    print("Text")
    print(a)
    print("{} {}".format(a, b))
    print(a, b)

  
# Loops

## for
    patterns = ["A", "B", "C"]

    for pattern in patterns: # 순회할 리스트가 있을때
      print(pattern)
  
    for i in range(5) # 0 <= i and i < 5 & 순회할 횟수가 정해져 있을때

    for i, pattern in enumerate(patterns): # index와 그 인덱스의 값을 반환한다.
      print('{}번 패턴 : {}'.format(i, pattern))
 
    for i in range(5) # 0 <= i and i < 5팬
    for i in range(5) # 0 <= i and i < 5
 
 
## while
    # while [참인 조건]:
    selected = None
    while selected not in ['A', 'B', 'C']:
        selected = input()
    
    print('selected value : ', selected)
    

## break, continue

    i = 2
    
    while True:
    
        i += 1
        
        if i == 6:
            break
        elif i == 3:
            continue
        
        print(i) # 4, 5

# Exception
## try, except
    """
    try:
        [예외가 발생할 가능성이 있는 코드]
    except [에러 종류 또는 Except as ex]:
        [예외를 처리할 코드]
    

    list1 = []
    list[0] # IndexError
    int("abc") # ValueError
    
    try:
        int("abc")
    except ValueError:
        print("not number")
        
    try:
        import my_Module
    except ImportError:
        print("don't exist")
        
## raise
    """
    raise [에러 종류]
    
    """
    i == 0
    if i == 0:
        raise ValueError

# 논리연산
    def getA():
        print("A")
        return False
        
    def getB():
        print("B")
        return True
    
    if getA() and getB():
        print(True)
    # getA() 함수는 호출되지만 False이기 때문에 __단락평가__로 인해 
    # getB() 함수는 호출되지 않는다.

# Class & Instance
## Class : 함수나 변수들을 모아 놓은 집합체. 현실의 개념을 표현.
#### self : 메소드의 첫번째 인자(자기 자신)이다
#### method : 함수와는 다르게 클래스에 묶여서 클래스 인스턴스와 관계되는 일을 하는 함수.
#### function(함수)를 사용한 경우
    class Human():
        '''인간'''

    def create(name, weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat(person):
        person.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다.".format(person.name, person.weight))

    def walk(person):
        person.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(person.name, person.weight))


    Human.create = create_human

    person = Human.create("Plutus", 70.5)

    Human.eat = eat
    Human.walk = walk

    person.walk()
    person.eat()
    person.walk()

#### method(메소드)를 사용한 경우
    class Human():
        '''인간'''

        def create(name, weight):
            person = Human()
            person.name = name
            person.weight = weight
            return person

        def eat(self):
            person.weight += 0.1
            print("{}가 먹어서 {}kg이 되었습니다.".format(person.name, person.weight))

        def walk(self):
            person.weight -= 0.1
            print("{}가 걸어서 {}kg이 되었습니다.".format(person.name, person.weight))


    person = Human.create("Plutus", 70.5)

    person.walk()
    person.eat()
    person.walk()


## 특수 메소드를 이용한 기본적인 Class 구조
#### __init__ : 인스턴스를 만들때 실행되는 함수. 클래스를 초기화하는 함수
#### __str__ : 인스턴스 자체를 출력할 때의 형식을 지정해주는 함수
    class Human():
            '''인간'''
            
            def __init__(self, name, weight):
                ''' 초기화 함수 '''
                self.name = name
                self.weight = weight
                
            def __str__(self):
                ''' 문자열과 함수 '''
                return "It's Human Class"

            def eat(self):
                person.weight += 0.1
                print("{}가 먹어서 {}kg이 되었습니다.".format(person.name, person.weight))

            def walk(self):
                person.weight -= 0.1
                print("{}가 걸어서 {}kg이 되었습니다.".format(person.name, person.weight))


        person = Human("Plutus", 70.2)
        print(person.name) # Plutus
        print(person.weight) # 70.2
        print(person) # It's Human Class


## Inheritance(상속)
#### class 자식 클래스명(부모 클래스명):
#### Override(오버라이드) : 부모가 가진 메소드를 같은 이름으로 덮어 쓴다는 의미
    class Animal():
        def walk(self):
            print("walk")
            
    class Human(Animal):
        # Override
        def walk(self):
            print("Human walk")
            
#### super() : 자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우
    class Animal():
        def __init__(self, name):
            self.name = name

        def greet(self):
            print("{} 이(가) 인사한다.".format(self.name))

    class Human(Animal):
        def __init__(self, name, hand):
            # 부모의 초기화 함수를 사용
            super().__init__(name)
            self.hand = hand
        def wave(self):
            print("{}을 흔들면서".format(self.hand))

        def greet(self):
            self.wave()
            super().greet()

    test = Human("Plutus", "Left")
    test.greet()


## Instance : 클래스에 의해 생성된 객체이고, 인스턴스 각자 자신의 값을 가지고 있다.


# Module
* 모듈은 미리 만들어진 코드를 가져와 쓰는 방법이다.
* import <모듈이름 또는 자신이 만든 파일 이름>    
    import math, random # built-in Module
