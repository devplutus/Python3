n = int(input())
arr = list(map(int, input().split()))
arr.sort()
_sum = []
for i in range(len(arr)):
    _sum.append(sum(arr[:i + 1]))

print(sum(_sum))