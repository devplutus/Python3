import queue
"""
BFS 사용
"""

def bfs(arr, start):
    q = queue.Queue()
    q.put(start)
    while q.queue:
        x, y = q.get()
        if arr[x][y][0] == 1 and arr[x][y][1] == False:

            arr[x][y][1] = True

            if x + 1 != len(arr) and arr[x + 1][y][0] == 1 and arr[x + 1][y][1] == False:
                q.put([x + 1, y])
            if x - 1 != -1 and arr[x - 1][y][0] == 1 and arr[x - 1][y][1] == False:
                q.put([x - 1, y])
            if y + 1 != len(arr[0]) and arr[x][y + 1][0] == 1 and arr[x][y + 1][1] == False:
                q.put([x, y + 1])
            if y - 1 != -1 and arr[x][y - 1][0] == 1 and arr[x][y - 1][1] == False:
                q.put([x, y - 1])


for t in range(int(input())):
    n, m, v = map(int, input().split())
    arr = [[[0, False] for i in range(n)] for j in range(m)]
    for i in range(v):
        y, x = map(int, input().split())
        arr[x][y][0] = 1
    
    count = 0
    for x in range(m):
        for y in range(n):
            if arr[x][y][0] == 1 and arr[x][y][1] == False:
                count += 1
                bfs(arr, [x, y])

    print(count)