n, m = map(int, input().split())

_min = 0
_max = 10000000000
answer = 0
arr = [int(input()) for i in range(n)]

while _min < _max - 1:
    _mid = (_max + _min) // 2
    total = 0
    for i in arr:
        total += i // _mid
    if total < m:
        _max = _mid
    else:
        _min = _mid

print(_min)