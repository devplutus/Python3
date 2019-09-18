N = int(input())
answer = []

# 최소 범위
_min = 1 if len(str(N)) == 1 else 10 * (len(str(N)) - 1)

for i in range(_min, N):
    _sum = i
    digit = list(str(i))
    for j in digit:
        _sum += int(j)

    if _sum == N:
        answer.append(i)

if answer:
    print(min(answer))
else:
    print(0)

