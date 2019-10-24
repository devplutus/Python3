import queue

n, m = map(int, input().split())
q = queue.Queue()

trunk = [[] for i in range(n + 1)]
indegree = [0 for i in range(n + 1)]
result = []

for i in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    trunk[a].append(b)

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.put(i)

while q.queue:
    c = q.get()

    for t in trunk[c]:
        if indegree[t] > 0:
            indegree[t] -= 1

        if indegree[t] == 0:
            q.put(t)
    result.append(c)

print(" ".join(map(str, result)))
