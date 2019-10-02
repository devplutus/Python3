n = int(input())
arr = {i : [0 for j in range(10)] for i in range(1, n+1)}
arr[1] = [1 for i in range(10)]
for i in range(2, n + 1):
    for j in range(10):
        if j - 1 >= 0:
            arr[i][j] += arr[i - 1][j - 1]
        if j + 1 <= 9:
            arr[i][j] += arr[i - 1][j + 1]

print(sum(arr[n][1:]) % 1000000000)

"""
- check -

0
01
010
012
0101
0121
0123

1
10
12
101
1012
1010
1010
1012
1210
1212
1232
1234

2
21
23
210
212
232
234
2101
2121
2123
2132
2134
2321
2324
2343
2345


"""