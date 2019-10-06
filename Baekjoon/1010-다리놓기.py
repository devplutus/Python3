import math
for i in range(int(input())):
    r, n = map(int, input().split())
    print(math.factorial(n) // (math.factorial(n - r) * math.factorial(r)))

"""
nCr 공식
n! //  (n - r)! r!
"""