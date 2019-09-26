import queue
"""
BFS 사용함
시작은 1번부터
"""

n = int(input())
m = int(input())
num = {i : [False, []] for i in range(1, n + 1)}
for i in range(m):
    a, b = map(int, input().split())
    num[a][1].append(b)
    num[b][1].append(a)


q = queue.Queue()
q.put(1)
count = 0
while q.queue:
    s = q.get()
    if num[s][0] == False:
        num[s][0] = True
        count += 1
        [q.put(i) for i in num[s][1]]

print(count - 1) # 1 자기 자신은 빼야됨.