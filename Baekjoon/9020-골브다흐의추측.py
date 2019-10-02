# 에라토스테네스의 체 사용
MAX = 10010
numbers = {i : True for i in range(1, MAX + 1)}
numbers[1] = False

for i in range(2, MAX // 2 + 1):
    if numbers[i] == False:
        continue
    for j in range(2, MAX // i + 1):
        numbers[i * j] = False

numbers = [i for i in numbers if numbers[i] == True]

T = int(input())

for i in range(T):
    n = int(input())
    mid = a // 2
    s, e = mid, mid

    while True:
        if prime[s] + prime[e] == n:
            print(prime[s], prime[e])
            break

        s -= 1
        e += 1
    