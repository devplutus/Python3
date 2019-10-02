n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split(" "))))

arr.sort(key=lambda k : (k[0], k[1]))

for i in arr:
    print(i[0], i[1])