n = int(input())
numbers = list(map(int, input().split()))
arr = {}
for i in range(n):
    arr[numbers[i]] = arr.get(numbers[i], 0) + 1
m = int(input())
find = list(map(int, input().split()))
result = []
for i in find:
    if i in arr:
        result.append(arr[i])
    else:
        result.append(0)
    
print(" ".join(map(str, result)))