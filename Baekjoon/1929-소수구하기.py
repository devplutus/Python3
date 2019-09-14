# 에라토스테네스의 체 사용
arr = list(map(int, input().split(" ")))

if arr[0] == 1:
    arr[0] += 1

numbers = {i : True for i in range(arr[0], arr[1] + 1)}

for i in range(2, arr[1] // 2 + 1):
    if i in numbers and numbers[i] == False:
        continue

    for j in range(2, arr[1] // i + 1):
        if i * j in numbers:
            numbers[i * j] = False
for j in [i for i in numbers if numbers[i] == True]:
    print(j)