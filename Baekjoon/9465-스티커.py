for i in range(int(input())):
    n = int(input())
    sticker = [list(map(int, input().split())) for i in range(2)]
    dp = [[0 for j in range(n)] for i in range(2)]
    dp[0][0], dp[1][0] = sticker[0][0], sticker[1][0]
    for j in range(1, n):
        if j == 1:
            dp[0][j] = sticker[0][j] + sticker[1][j - 1]
            dp[1][j] = sticker[1][j] + sticker[0][j - 1]
        else:
            dp[0][j] = max(dp[1][j - 2], dp[1][j - 1]) + sticker[0][j]
            dp[1][j] = max(dp[0][j - 2], dp[0][j - 1]) + sticker[1][j]

    print(max(dp[0][-1], dp[1][-1]))

        

"""

100     40
    10          k - 1 + k

100     
        60     : k - 2 + k

    20  40
70  10  60

x3 + y2 + x1
x3 + y1
"""