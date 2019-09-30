n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

_sum = [0 for i in range(n)]
_sum[0] = arr[0]

for i in range(1, n):
    if i < 3:
        if i == 1:
            _sum[i] = arr[0] + arr[1]
        else:
            _sum[i] = max(_sum[0] + arr[i], arr[i - 1] + arr[i])
    else:
        _sum[i] = max(_sum[i - 3] + arr[i - 1] + arr[i], _sum[i - 2] + arr[i])

print(_sum)

"""
8   3   5   8   1
            c
o       o   o       : check 1
    o       o       : check 2

"""