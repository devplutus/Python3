def find(n, arr, _3, _5, is_3):
    if n in (0, 1):
        if n == 0:
            arr.append([_3, _5])
        return
    elif not is_3 and n % 3 != 0:
        return
    elif is_3 and n % 5 != 0:
        return
    for i in [3, 5]:
        if i == 3:
            find(n % i, arr, n // 3, _5, True)
        else:
            find(n % i, arr, _3, n // 5, False)

n = int(input())
a = []
find(n, a, 0, 0, True)
print(a)

