" 총 해결 시간 : 약 1시간"

def cal (value1, value2, exp):
    if exp == "+":
        return value1 + value2
    elif exp == "-":
        return value1 - value2
    elif exp == "*":
        return value1 * value2
    else:
        return 0

n = int(input())
_str = input()
_exp = []
_num = []
_sum = [[] for i in range(20)]

for i, v in enumerate(_str):
    if i % 2 == 1:
        _exp.append(v)
    else:
        _num.append(int(v))

_sum[0].append(_num[0])

for i in range(1, len(_num)):

    for s in _sum[i - 1]:
        _sum[i].append(cal(s, _num[i], _exp[i - 1]))

    if i - 2 >= 0:
        first = cal(_num[i - 1], _num[i], _exp[i - 1])
        for s in _sum[i - 2]:
            _sum[i].append(cal(s, first, _exp[i - 2]))

print(max(_sum[len(_num) - 1]))