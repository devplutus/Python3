

total = int(input())

for i in range(total):
    k = int(input())
    n = int(input())
    floor = [i for i in range(1, n + 1)]
    for j in range(k):
        temp_floor = [i for i in floor]
        for x in range(n):
            floor[x] = sum(temp_floor[:x + 1])
            print(floor)
            

    print(floor[n - 1])

"""
4   1   6   21
3   1   5   15
2   1   4   10  20  35  56  84  1
1   1   3   6   10  15  21  28  36
0   1   2   3   4   5   6   7   8
"""