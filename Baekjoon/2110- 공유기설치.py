n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
s = 1
e = n
answer = 0
while s < e - 1:
    mid = (s + e) // 2
    total = 1
    index = 0
    for i in range(1, len(arr)):
        if arr[i] - arr[index] >= mid:
            index = i
            total += 1
    if m >= total:
        s = mid
    else:
        e = mid
    if total >= m and answer < mid:
        answer = total

print(total)