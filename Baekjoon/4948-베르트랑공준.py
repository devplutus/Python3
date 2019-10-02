# 에라토스테네스의 체 사용
MAX = 123456 * 2
numbers = {i : True for i in range(1, MAX + 1)}
numbers[1] = False

for i in range(2, MAX // 2 + 1):
    if numbers[i] == False:
        continue
    flag = True
    for j in range(2, MAX // i + 1):
        numbers[i * j] = False

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n + 1, n * 2 + 1):
        if numbers[i] == True:
            count += 1

    print(count)