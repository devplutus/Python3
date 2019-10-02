import heapq, sys

n = int(sys.stdin.readline())
_min = []
_max = []
for i in range(n):
    c = int(sys.stdin.readline())

    if len(_min) == len(_max):
        heapq.heappush(_min, (-c, c))
    else:
        heapq.heappush(_max, c)

    if len(_max) and _min[0][1] >= _max[0]:
            heapq.heappush(_max, heapq.heappop(_min)[1])
            m = heapq.heappop(_max)
            heapq.heappush(_min, (-m, m))

    s = heapq.heappop(_min)
    print(s[1])
    heapq.heappush(_min, s)


"""
5444332
L           R
5           
4           5
4 4         5
4 4 4       5
4 4 4       5 3

"""