import queue

def dfs(arr, start, result):
    if arr[start][0] == True:
        return
    else:
        arr[start][0] = True
        result.append(start)
        for c in arr[start][1]:
            dfs(arr, c, result)

def bfs(arr, start, result):
    q = queue.Queue()
    q.put(start)
    while q.queue:
        a = q.get()
        if arr[a][0] == False:
            arr[a][0] = True
            result.append(a)
            [q.put(i) for i in arr[a][1]]

n, m, v = map(int, input().split())
arr = {i : [False, []] for i in range(1, n + 1)}
for i in range(m):
    a, b = list(map(int, input().split()))
    arr[a][1].append(b)
    arr[b][1].append(a)
for i in range(1, n + 1):
    arr[i][1].sort()

dfs_Result = []
bfs_Result = []

dfs(arr, v, dfs_Result)
for i in range(1, n + 1):
    arr[i][0] = False
bfs(arr.copy(), v, bfs_Result)

print(" ".join(map(str, dfs_Result)))
print(" ".join(map(str, bfs_Result)))

"""
x : [False, [...]] ([방문여부, [자식들]])

BFS(Breath First Search) : 넓이 우선 탐색
- Queue 이용

DFS(Depth First Search) : 깊이 우선 탐색
- 재귀 사용
"""