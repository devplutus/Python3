_sum = 0
for i in range(5):
    n = int(input())
    if n < 40:
        _sum += 40
    else:
        _sum += n
print(_sum // 5)
