a = list(map(int,input().split()))

dp = [[0 for i in range(len(a))] for j in range(len(a))]

for i in range(len(a)):
    for j in range(len(a)):
        if i != j:
            dp[i][j] = a[i] + a[j]

for i in dp:
    print(i)
