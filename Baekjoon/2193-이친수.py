n = int(input())

fibonacci = [1, 1, 2]

if n < 3:
    print(fibonacci[n - 1])
else:
    s = 3
    while s < n:
        fibonacci[:2] = fibonacci[1:]
        fibonacci[-1] = sum(fibonacci[:2])
        s += 1
    
    print(fibonacci[-1])

"""
피보나치 수열
1
1

2
10

3
100
101

4
1000
1001
1010

5
10000
10001
10010
10100
10101
"""