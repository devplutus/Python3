import queue
for i in range(int(input())):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    m_Priority = priority[m]
    q = queue.Queue()
    
    for i in range(n):
        q.put([priority[i], i])

    c = 0
    while True:
        isFind = False
        _max = max(q.queue)
        while True:
            v = q.get()
            if _max[0] == m_Priority and v[1] == m:
                c += 1
                isFind = True
                print(c)
                break
            elif v[0] == _max[0]:
                c += 1
                break
            else:
                q.put(v)
        
        if isFind:
            break