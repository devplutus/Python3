def hanoi(n, s, b, e, i):
    if n == 1:
        i.append([s, e])
        return 0
    hanoi(n - 1, s, e, b, i)
    i.append([s, e])
    hanoi(n - 1, b, s, e, i)

n = int(input())

a = []
hanoi(n, 1, 2, 3, a)
print(len(a))
for v in a:
    print(v[0], v[1])