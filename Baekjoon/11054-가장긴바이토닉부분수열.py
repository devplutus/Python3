def find(arr):
    _sum = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        _max = 0
        for j in range(len(arr)):
            if arr[j] < arr[i] and _sum[j] > _max:
                _max = _sum[j]

        _sum[i] = _max + 1
    return _sum

n = int(input())
arr = list(map(int, input().split()))
L_sum = find(arr)
arr.reverse()
R_sum = find(arr)
R_sum.reverse()

_max = 0
for i in range(n):
    _sum = L_sum[i] + R_sum[i]
    if _max < _sum:
        _max = _sum

print(_max - 1)
