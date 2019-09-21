def isExist(arr, n, s, e):
    if s == e - 1:
        if arr[s] == n or arr[e] == n:
            return 1
        else:
            return 0
    else:
        mid = (s + e) // 2
        if arr[mid] == n:
            return 1
        elif arr[mid] < n:
            result = isExist(arr, n, mid, e)
        else:
            result = isExist(arr, n, s, mid)

        return result



n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
find = list(map(int,input().split()))

for i in find:
    print(isExist(arr, i, 0, len(arr) - 1))