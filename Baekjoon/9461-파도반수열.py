for i in range(int(input())):
    arr = [1, 1, 1, 2]
    n = int(input())
    if n < 4:
        print(1)
    else:
        s = 4
        while s < n:
            a4 = arr[1] + arr[2]
            arr[:3] = arr[1:]
            arr[-1] = a4
            s += 1

        print(arr[-1])