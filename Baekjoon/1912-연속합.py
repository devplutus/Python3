n = int(input())
arr = list(map(int, input().split()))

_sum = [[] for i in range(n)]
_sum[0] = arr[0]

for i in range(1, n):
    _sum[i] = max(arr[i], _sum[i - 1] + arr[i])
    
print(max(_sum))