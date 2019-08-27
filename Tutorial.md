# String

String1 = 'string1'
String2 = "string2"
StringFormat = "{} + {}"
StringFormat.format(String1, String2) # strgin1 + string2
String3 = """ " and ' """ # " and '


# Number

num1 = 3 # int
num2 = 3.0 # float
num3 = 4 / 4 # 1.0(float)
num4 = 4 // 4 # 1(int)
num5 = 12 % 5 # 2(int)

num1 = float(num1) # 3.0(float)
num2 = int(num2) # 3(int)


# Input

a = input("Type") # == print("Type")
                       a = input()
                      
  
 
# for문
patterns = ["A", "B", "C"]

for pattern in patterns: # 순회할 리스트가 있을때
  print(pattern)
  
for i in range(5) # 0 <= i and i < 5 & 순회할 횟수가 정해져 있을때

for i, pattern in enumerate(patterns): # index와 그 인덱스의 값을 반환한다.
  print('{}번 패턴 : {}'.format(i, pattern))
 
for i in range(5) # 0 <= i and i < 5팬
for i in range(5) # 0 <= i and i < 5
 
 
 
# Module
* 모듈은 미리 만들어진 코드를 가져와 쓰는 방법이다.
* import <모듈이름 또는 자신이 만든 파일 이름>
import math, random # built-in Module


# List

list1 = [0, 1, 2, 3, 4, 5] # size = 6
list1[-1] # 5(뒤에서 첫번째)
list1[-7] # Excpetion : out of range

list2 = 6
list1 = list1 + list2 # == list1.append(6) ([0, 1, 2, 3, 4, 5, 6])
del list1[-1] # == del(list[-1]) == list1.remove(6) ([0, 1, 2, 3, 4, 5])

find = 3


if find in list1: # list1 안에 3이 있는지 확인.
  print("Exist")
  

# Dictionary
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
  
  
# Dictionary 와 List 차이점
*   합치기
list1 = [0, 1, 2, 3]
list2 = list + [4, 5, 6]

dic1 = {'one':1, 'two', 2}
dic2 = {'three':3, 'four',4}
di1.update(dic2)
* 찾기
1 in list1
'one' in dic1.keys()
2 in dic1.values()



# Tuple
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
