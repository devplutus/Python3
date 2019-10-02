import heapq, sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    c = int(sys.stdin.readline())
    if c == 0:
        if len(arr):
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr, (-c, c))

