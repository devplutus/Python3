from sys import stdin

n = int(stdin.readline())
arr = [0 for i in range(10001)]

for i in range(n):
    arr[int(stdin.readline())] += 1

for i, v in enumerate(arr):
    if v != 0:
        [print(i) for j in range(v)]
