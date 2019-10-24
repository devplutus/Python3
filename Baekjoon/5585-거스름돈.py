n = 1000 - int(input())
result = 0

_num = [500, 100, 50, 10, 5, 1]

for i in range(len(_num)):
    result += n // _num[i]

    if n % _num[i] == 0:
        break
    else:
        n = n % _num[i]

print(result)
