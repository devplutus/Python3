n, k = int(input()), int(input())

s = 1
e = n * n
answer = 0
while s <= e:
    mid = (s + e) // 2

    total = 0
    check = False
    for i in range(1, n + 1):
        if mid > i * n:
            total += n
        else:
            total += mid // i

    if total >= k:
        e = mid - 1
        answer = mid
    elif total < k:
        s = mid + 1

print(answer)
"""
1   2   3
2   4   6
3   6   9

1 2 2 3 3 4 6 6 9
"""