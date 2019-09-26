import sys
"""
BFS 이용
"""
n, m = map(int, sys.stdin.readline().split())
_map = [[[int(j), False] for j in sys.stdin.readline().strip()] for i in range(n)]

_map[0][0][1] = True

x_way = [1, -1, 0, 0]
y_way = [0, 0, 1, -1]

_next = [[0, 0, False]]
result = 0
find = False
isBroken = False
while _next:
    child = _next
    _next = []
    result += 1
    for c in child:

        for w in range(4):
            x = c[0] + x_way[w]
            y = c[1] + y_way[w]
            isBroken = c[2]
            if x == n - 1 and y == m - 1:
                find = True
                break

            if x in (-1, n) or y in (-1, m):
                continue

            if _map[x][y][0] == 0 and _map[x][y][1] == False:
                _map[x][y][1] = True
                _next.append([x, y, isBroken])

    if len(_next) == 0 and isBroken == False:
        for w in range(4):
            x = c[0] + x_way[w]
            y = c[1] + y_way[w]

            if x in (-1, n) or y in (-1, m):
                continue

            if _map[x][y][1] == False:
                _map[x][y][0] = 0
                _next.append([x, y, isBroken])
        isBroken = True
        
    if find:
        _next = []

if find:
    print(result + 1)
else:
    print("-1")

0011
0000
1111
0010
1000