M = int(input())
N = int(input())
numbers = []

if M == 1:
    M += 1

for i in range(M, N + 1):
    flag = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            flag = False
            break
    if flag:
        numbers.append(i)

if numbers:
    print(sum(numbers))
    print(min(numbers))
else:
    print("-1")