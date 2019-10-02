n = int(input())

arr = {1 : 0}
count = 0
for i in range(2, n + 1):
    result = []
    if i % 2 == 0:
        result.append(arr[i // 2] + 1)
    if i % 3 == 0:
        result.append(arr[i // 3] + 1)
    result.append(arr[i - 1] + 1)

    arr[i] = min(result)

print(arr[n])
    

"""
1
2 -> 1
3 -> 1
4 -> 2 -> 1
4 -> 3 -> 1
5 -> 4 -> 2 -> 1
6 -> 3(2) -> 1
7 -> 6 -> 3(2) -> 1
8 -> 4 -> 2 -> 1
9 -> 3 -> 1
10 -> 9 -> 3 -> 1
11 -> 10 -> 9 -> 3 -> 1
12 -> 6 -> 2 -> 1
12 -> 4 -> 2 -> 1
"""
