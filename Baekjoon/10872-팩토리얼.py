# math Library 사용
import math
n = int(input())
print(math.factorial(n))

# 구현
def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return n * (factorial(n-1))

print(factorial(n))
