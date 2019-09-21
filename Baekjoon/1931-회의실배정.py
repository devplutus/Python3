import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key = lambda k:(k[1], k[0]))

s = 0
c = 0
for i in range(n):
    if s <= arr[i][0]:
        s = arr[i][1]
        c += 1

print(c)
