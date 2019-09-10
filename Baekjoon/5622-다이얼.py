numbers = {
    2:"ABC",
    3:"DEF",
    4:"GHI",
    5:"JKL",
    6:"MNO",
    7:"PQRS",
    8:"TUV",
    9:"WXYZ",
    }

_sum = 0

for c in input():
    second = 2
    for k, v in numbers.items():
        if c in v:
            second += 1 * (k - 1)
            break
    _sum += second

print(_sum)