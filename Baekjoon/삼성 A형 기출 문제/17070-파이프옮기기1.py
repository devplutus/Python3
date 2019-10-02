"""
총 해결 시간 : 약 1시간 40분
BFS로 뻘짓하다가 DFS로 새로 구현해서 해결
BFS로 되는데 구현을 이상하게 해서 시간 초과
개념은 알고있었으니 뻘짓 ㄴㄴ
"""

import sys

n = int(sys.stdin.readline())
tiles = [[int(i) for i in sys.stdin.readline().split()] for i in range(n)]

def dfs(arr, x, y, w):
    if x == n - 1 and y == n - 1:
        return 1
    result = 0
    if (w == 0 or w == 2) and y + 1 != n and arr[x][y + 1] == 0:
        result += dfs(arr, x, y + 1, 0)
    
    if (w == 1 or w == 2) and x + 1 != n and arr[x + 1][y] == 0:
        result += dfs(arr, x + 1, y, 1)
    
    if x + 1 != n and y + 1 != n:
        if arr[x + 1][y] == 0 and arr[x][y + 1] == 0 and arr[x + 1][y + 1] == 0:
            result += dfs(arr, x + 1, y + 1, 2)
    return result

print(dfs(tiles, 0, 1, 0))