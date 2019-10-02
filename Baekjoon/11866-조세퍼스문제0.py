n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]
s = k - 1
result = []
for i in range(n-1):
    result.append(arr[s])
    arr[s] = 0
    c = 0
    while True:
        if s + 1 == len(arr):
            s = 0
        else:
            s += 1
        if arr[s] != 0:
            c += 1
        if c == k:
            break
result = result + [i for i in arr if i != 0]

#  <?, ?, ?,...?> 형식으로 변환
_str = "<"
for i in range(len(result)):
    if i != len(result) - 1:
        _str += "{}, ".format(result[i])
    else:
        _str += "{}>".format(result[i])

print(_str)
"""
1234567
0123456

2
5
1

"""
