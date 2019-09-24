import sys
n, m = map(int, sys.stdin.readline().split())
woods = list(map(int, sys.stdin.readline().split()))
woods.sort(reverse=True)
answer, _min, _max, _sum = 0, 0, max(woods), sum(woods)
check = False
while _min <= _max:
    _mid = (_min + _max) // 2
    
    total = _sum
    for i in woods:
        if i >= _mid:
            total -= _mid
        else:
            total -= i

    if total == m:
        check = True
        answer = _mid
        break

    if total < m:
        _max = _mid - 1
    else:
        _min = _mid + 1

if check:
    print(answer)
else:
    print((_min + _max) // 2)

