n = int(input())
arr = []
_sum = [0 for i in range(n)]
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:x[0])

for i in range(n):
    _max = 0
    for j in range(i):
        if arr[i][1] > arr[j][1] and _max < _sum[j]:
            _max = _sum[j]
    
    _sum[i] = _max + 1

print(n - max(_sum))