n = int(input())
arr = [[0, 0] for i in range(n)]
dp = [0 for i in range(n)]

for i in range(n):
    t, p = map(int, input().split())
    arr[i][0] = t
    arr[i][1] = p

if n == 1 and arr[0][0] == 1:
    dp[0] = arr[0][1]

for i in range(n):

    next_Day = i + arr[i][0]

    if next_Day < n or i == n - 1 and arr[i][0] == 1:

        if dp[i] == 0:
            dp[i] = arr[i][1]

        for j in range(next_Day, n):
            if j + arr[j][0] - 1 < n or (j == n - 1 and arr[j][0] == 1):
                dp[j] = max(dp[j], dp[i] + arr[j][1])

print(max(dp))


"""
0   1   2   3   4   5   6   7   8   9
5   4   3   2   1   1   2   3   4   5
50  40  30  20  10  10  20  30  40  50

50                  60
    40              50
        30          40
            20      30
                10  20

                    60  80
                    60      90
                              

"""