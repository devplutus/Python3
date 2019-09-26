import queue
"""
최단경로 BFS 사용
"""

def bfs(arr, index):
    q = queue.Queue()
    q.put(index)
    c = arr.copy()
    while q.queue:
        x, y = q.get()
        if arr[x][y][0] == 1 and arr[x][y][1] == False:
            arr[x][y][1] = True
            count = arr[x][y][2] + 1
            if x + 1 != len(arr) and arr[x + 1][y][0] == 1 and arr[x + 1][y][1] == False:
                check(arr, q, [x + 1, y], count)
            if x - 1 != -1 and arr[x - 1][y][0] == 1 and arr[x - 1][y][1] == False:
                check(arr, q, [x - 1, y], count)
            if y + 1 != len(arr[0]) and arr[x][y + 1][0] == 1 and arr[x][y + 1][1] == False:
                check(arr, q, [x, y + 1], count)
            if y - 1 != -1 and arr[x][y - 1][ 0] == 1 and arr[x][y - 1][1] == False:
                check(arr, q, [x, y - 1], count)
            """
            for i in range(len(arr)):
                print("\t".join(map(str, [j[2] for j in arr[i]])))
            print("----------------------")
            """

def check(arr, q, index, count):
    x, y = index
    if q.queue.count([x, y]) == 0:
        q.put([x, y])
        arr[x][y][2] += count



n, m = map(int, input().split())
arr = []
result = []
for i in range(n):
    arr.append([[int(i), False, 0] for i in input()])
bfs(arr, [0, 0])
print(arr[n - 1][m - 1][2] + 1)