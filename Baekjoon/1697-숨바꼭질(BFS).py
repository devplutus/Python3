_MAX = 100000
s, e = map(int, input().split())

if e <= s:
    print(abs(e - s)) # 절댓값으로~
else:
    nums = [False for i in range(_MAX + 1)]

    result = 0
    _next = []
    _next.append(s)
    while _next:

        child = _next
        _next = []

        for c in child:
            if c < 0 or c > _MAX:
                continue

            w1 = c - 1
            w2 = c + 1
            w3 = c * 2

            if w1 == e or w2 == e or w3 == e:
                _next = []
                result += 1
                break
            
            if w1 >= 0 and w1 <= _MAX and nums[w1] == False:
                nums[w1] = True
                _next.append(w1)
            if w2 >= 0 and w2 <= _MAX and nums[w2] == False:
                nums[w2] = True
                _next.append(w2)
            if w3 >= 0 and w3 <= _MAX and nums[w3] == False:
                nums[w3] = True
                _next.append(w3)

        if _next:
            result += 1

    print(result)


