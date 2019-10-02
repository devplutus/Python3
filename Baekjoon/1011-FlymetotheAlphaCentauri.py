n = int(input())

for i in range(n):
    arr = list(map(int, input().split(" ")))
    s = arr[0] + 1
    e = arr[1] - 1
    c = 0
    k = 1
    while True:
        if s == e:
            print(c + 1)
            break
        s += k
        print("k={} s={} e={} 남은거리={}".format(k, s, e, e - s - 1))
        if e - s - 1 == k:

            k -= 1
        elif e - s  - 1> 1:
            k += 1
        c += 1

