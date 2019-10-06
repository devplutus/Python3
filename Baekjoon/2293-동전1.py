n, k = map(int, input().split())

dp = [[0 for i in range(n)] for i in range(k + 1)]
numbers = [int(input()) for i in range(n)]
numbers.sort()

for i in range(1, k + 1):
    for j in range(n):
        if numbers[j] > i:
            break
        elif numbers[j] == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - numbers[j]][j]
        print(i, j)

print(dp)


"""
n = 10
1 2 5

1
1

2
1 1
2

3
1 1 1
2 1

4
1 1 1 1
2 1 1
2 2

5
1 1 1 1 1
2 1 1 1
2 2 1
5

6
1 1 1 1 1 1
2 1 1 1 1
2 2 1 1
2 2 2
5 1

7
1 1 1 1 1 1 1
2 1 1 1 1 1
2 2 1 1 1
2 2 2 1
5 1 1
5 2

8
1 1 1 1 1 1 1 1
1 1 1 1 1 1 2
1 1 1 1 2 2
1 1 2 2 2
2 2 2 2
5 1 1 1
5 1 2





"""