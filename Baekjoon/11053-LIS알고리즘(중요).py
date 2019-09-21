input()
arr = list(map(int, input().split()))
_sum = [0 for i in range(len(arr))]

for i in range(len(arr)):
    _max = 0
    for j in range(i):
        if arr[i] > arr[j] and _sum[j] > _max:
            _max = _sum[j]
    _sum[i] = _max + 1

print(max(_sum))


"""
1
11 13 15 18 23 14 12 11 16 24 32 17

이전 값들 중 자신의 값보다 작고 빈도수가 높은 값 + 자기 자신

"""