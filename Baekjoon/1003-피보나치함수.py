n = int(input())

for i in range(n):

    f = int(input())
    c0 = [1, 0]
    if f == 0:
        print(c0[0], c0[1])
        continue
    c1 = [0, 1]
    if f == 1:
        print(c1[0], c1[1])
        continue

    c2 = [c0[0] + c1[0], c0[1] + c1[1]]
    s = 2
    while s < f:
        c0, c1 = c1, c2
        c2 = [c0[0] + c1[0], c0[1] + c1[1]]
        s += 1

    print(c2[0], c2[1])