n = int(input())

s = [1, 2, 3]

if n <= 3:
    print(s[n - 1])
else:
    start = 3

    while start < n:
        s[:2] = s[1:]
        s[2] = sum(s[:2])
        start += 1

    print(s[-1] % 10007)

