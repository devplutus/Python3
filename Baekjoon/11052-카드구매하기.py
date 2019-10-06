n = int(input())
card = list(map(int, input().split()))
_sum = [0 for i in range(n + 1)]
_sum[1] = card[1]

for i in range(1, n + 1):
    _max = card[i - 1]
    for j in range(i - 1, 0, -1):
        if _sum[j] + _sum[i - j] > _max:
            _max = _sum[j] + _sum[i - j]

    _sum[i] = _max
        
    
print(_sum[-1])
    
"""
1 5 6 7

1
1

2
1 1
5
sum(2) = sum(2)

3
1 1 1
1 5
6
sum(3) = sum(2) + sum(1) = sum(1) + sum(1)

4
1 1 1 1
1 1 5
5 5
6 1
7
sum(4) = sum(3) = sum(2) + sum(1)

"""