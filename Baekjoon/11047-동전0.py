n, k = map(int, input().split())
arr = []
for i in range(n):
    value = int(input())
    if value < k:
        arr.append(value)

count = 0

while k != 0:
    count += k // arr[-1]
    k = k % arr[-1]
    arr.pop()

print(count)
    

