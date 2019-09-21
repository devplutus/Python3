n = int(input())
arr = [int(input()) for i in range(n)]
arr.sort()
_max = 0

for i in range(n):
    if _max < arr[i] * (n - i):
        _max = arr[i] * (n - i)

print(_max)

"""
w = rope_W의 최소값 * k
각 로프의 최소값에 맞춰서 찾자
"""
