n = int(input())
dp = [[0 for i in range(10)] for i in range(1002)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, 1002):
    for j in range(0, 10):
        dp[i][j] = sum(dp[i - 1][j:])

print(dp[n+1][0] % 10007)


"""
1

dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1
dp[1][3] = 1
dp[1][4] = 1
dp[1][5] = 1
dp[1][6] = 1
dp[1][7] = 1
dp[1][8] = 1
dp[1][9] = 1

"""
