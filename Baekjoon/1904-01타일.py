n = int(input())
arr = [1, 2, 3]
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[1])
else:
    s = 3
    for i in range(n - s):
        arr[0] = arr[1]
        arr[1] = arr[2]
        arr[2] = (arr[1] + arr[0]) % 15746

    print(arr[-1])
