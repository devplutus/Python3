n = input()
arr = list(map(int, input().split(" ")))
count = 0
for i in arr:
    if i == 1:
        continue
    flag = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            flag = False
            break
    if flag:
        count += 1

print(count)