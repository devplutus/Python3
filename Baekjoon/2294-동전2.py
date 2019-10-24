n, k = map(int, input().split())

_num = [int(input()) for i in range(n)]
_num.sort()
_dp = [0 for i in range(k + 1)]

for i in range(1, k + 1):
    for j in range(n):
        if _num[j] > i:
            continue
        else:
            if i % _num[j] == 0:
                if _dp[i] == 0:
                    _dp[i] = i // _num[j]
                else:
                    _dp[i] = min(_dp[i], i // _num[j])
            else:
                if _dp[i - _num[j]] != 0:
                    if _dp[i] == 0:
                        _dp[i] = _dp[i - _num[j]] + 1
                    else:
                        _dp[i] = min(_dp[i], _dp[i - _num[j]] + 1)

if _dp[k] == 0:
    print("-1")
else:
    print(_dp[k])

"""
2 3

1 - 0
-

2 - 1
2

3 - 1
3

4 - 2
2 2

5 - 2
2 3

6 - 2
2 2 2
3 3

7 - 3
2 2 3

8 - 3
2 2 2 2
3 3 2

9 - 3
2 2 2 3
3 3 3

10 - 4
2 2 2 2 2
3 3 2 2


"""
