n, m = map(int, input().split())
arr = [[0]] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))

x = int(input())

for s in range(x):
    i, j, x, y = map(int, input().split())
    _sum = 0
    for a in range(i - 1, x):
        _sum += sum(arr[a][j - 1: y])

    print(_sum)
