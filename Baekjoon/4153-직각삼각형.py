while True:
    arr = list(map(int, input().split(" ")))
    arr.sort()
    a, b, c = arr
    if sum(arr) == 0:
        break
    else:
        a **= 2
        b **= 2
        c **= 2
        if a + b == c:
            print("right")
        else:
            print("wrong")

