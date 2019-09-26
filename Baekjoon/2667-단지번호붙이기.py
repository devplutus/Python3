import queue
"""
BFS 사용
"""
def bfs(arr, start):
    q = queue.Queue()
    q.put(start)
    result = 0
    while q.queue:
        i, j = q.get()
        if arr[i][j][1] == False:
            arr[i][j][1] = True
            result += 1
            if i + 1 != len(arr) and arr[i + 1][j][0] == 1 and arr[i + 1][j][1] == False:
                q.put([i + 1, j])
            if i - 1 != -1 and arr[i - 1][j][0] == 1 and arr[i - 1][j][1] == False:
                q.put([i - 1, j])
            if j + 1 != len(arr) and arr[i][j + 1][0] == 1 and arr[i][j + 1][1] == False:
                q.put([i, j + 1])
            if j - 1 != -1 and arr[i][j - 1][0] == 1 and arr[i][j - 1][1] == False:
                q.put([i, j - 1])
    return result

n = int(input())

arr = []
for i in range(n):
    arr.append([[int(i), False] for i in input()])
    # [0 or 1, 방문여부]

count = 0
house = []
for i in range(n):
    for j in range(n):
        if arr[i][j][0] == 1 and arr[i][j][1] == False:
            count += 1
            house.append(bfs(arr, [i, j]))

print(count)
[print(i) for i in sorted(house)]
