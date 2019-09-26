import sys
"""
BFS 사용
"""

def bfs(tomato, visited, start, tomato_cnt, n, m):
    # 하, 상, 우, 좌
    x_way = [1, -1 ,0, 0]
    y_way = [0, 0, 1, -1]

    result = 0
    tomato_cnt += len(start)

    _next = start

    while _next:
        child = _next.copy()
        _next = []

        for c in child:
            x, y = c
            tomato[x][y] = 1
            visited[x][y] = True
            tomato_cnt -= 1

            for w in range(4):
                if x + x_way[w] in (-1, n) or y + y_way[w] in (-1, m):
                    continue
                else:
                    if tomato[x + x_way[w]][y + y_way[w]] == 0 and visited[x + x_way[w]][y + y_way[w]] == False:
                        tomato[x + x_way[w]][y + y_way[w]] = 1
                        visited[x + x_way[w]][y + y_way[w]] = True
                        _next.append([x + x_way[w], y + y_way[w]])
        if _next:
            result += 1

    if tomato_cnt == 0:
        return result
    else:
        return -1

m, n = map(int, sys.stdin.readline().split())
tomato = [[int(j) for j in sys.stdin.readline().split()] for i in range(n)]
visited = [[False for i in range(m)] for i in range(n)]
start = []
tomato_cnt = 0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            start.append([i, j])
        elif tomato[i][j] == 0:
            tomato_cnt += 1

print(bfs(tomato, visited, start, tomato_cnt, n, m))

