n = int(input())
arr = []
for i in range(n):
    arr.append(input())
arr = list(set(arr))
arr.sort(key = lambda k:(len(k), k))
for i in arr:
    print(i)