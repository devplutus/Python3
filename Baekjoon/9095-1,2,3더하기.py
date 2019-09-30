"""
1, 2 ,4, 7, 13
"""
for i in range(int(input())):
    n = int(input())

    a = [1, 2, 4, 7]
    if n <= 4:
        print(a[n - 1])
    else:
        s = 5
        while s <= n:
            a[:3] = a[1:]
            a[3] = sum(a[:3])
            s += 1
        
        print(a[-1])
