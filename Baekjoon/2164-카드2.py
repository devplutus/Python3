n = int(input())
s = 1
while True:
    if s * 2 > n:
        break
    else:
        s *= 2
if n == s:
    print(s)
else:
    print(n - (s - (n - s)))

"""
I O G
1 1 0
2 2 0
3 2 1
4 4 0
5 2 3
6 4 2
7 6 1
8 8 0
9 2 7
10 4 6
11 6 5
12 8 4
13 10 3
14 12 2
15 14 1
16 16 0
17 2 15
18 4 14
19 6 13
"""
