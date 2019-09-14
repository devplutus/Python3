n = int(input())
for i in range(n):
    arr = list(map(int, input().split(" ")))
    M = arr[0]
    N = arr[1]
    x1 = arr[2]
    y1 = arr[3]

    x = 1
    y = 1
    count = 1

    flag = True
    while True:
        if x == x1 and y == y1:
            flag = False
            print(count)
            break
        if x == M and y == N:
            break
        x = x + 1 if x < M else 1
        y = y + 1 if y < N else 1
        count += 1
    if flag:
        print("-1")