from sys import stdin
from collections import Counter

n = int(input())

arr = []
for i in range(n):
    arr.append(int(stdin.readline()))
arr.sort()

# 평균
average = sum(arr) / n
# 최빈값
mode = dict(Counter(arr))
_max = max(mode.values())
modes = []
for k in mode:
    if mode[k] == _max:
        modes.append(k)

if len(modes) == 1:
    mode = modes[0]
else:
    modes.sort()
    mode = modes[1]

# 중앙값
mid = arr[n // 2]
# 범위
_range = arr[-1] - arr[0]

print(round(average))
print(mid)
print(mode)
print(_range)
