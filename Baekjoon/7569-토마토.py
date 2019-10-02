import sys

def bfs(arr, visited, start, tomato_cnt, n, m, h):
    x_way = [1, -1, 0, 0, 0, 0]
    y_way = [0, 0, 1, -1, 0, 0]
    z_way = [0, 0, 0, 0, 1, -1]

    tomato_cnt += len(start)
    result = 0

    _next = start

    while _next:
        child = _next
        _next = []
        for c in child:
            x, y, z = c
            tomato_cnt -= 1
            for w in range(6):
                x1 = x + x_way[w]
                y1 = y + y_way[w]
                z1 = z + z_way[w]
                if x1 in (-1, n) or y1 in (-1, m) or z1 in (-1, h):
                    continue
                
                if tomatos[x1][y1][z1] == 0 and visited[x1][y1][z1] == False:
                    tomatos[x1][y1][z1] = 1
                    visited[x1][y1][z1] = True
                    _next.append([x1, y1, z1])

        if _next:
            result += 1

    if tomato_cnt == 0:
        return result
    else:
        return -1

y, x, z = map(int, sys.stdin.readline().split())
tomatos = [[[[] for l in range(z)] for j in range(y)] for i in range(x)]
visited = [[[False for l in range(z)] for j in range(y)] for i in range(x)]
start = []
tomato_cnt = 0
for l in range(z):
    for i in range(x):
        tomato = list(map(int, sys.stdin.readline().split()))
        for j in range(y):
            tomatos[i][j][l] = tomato[j]
            if tomato[j] == 1:
                start.append([i, j, l])
            elif tomato[j] == 0:
                tomato_cnt += 1


print(bfs(tomatos, visited, start, tomato_cnt, x, y, z))