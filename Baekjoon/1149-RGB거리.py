n = int(input())
house = []
for i in range(n):
    house.append(list(map(int, input().split())))

_sum = [[0, 0, 0] for i in range(n)]
_sum[0] = house[0]
for i in range(1, n):
    _sum[i][0] = house[i][0] + min(_sum[i - 1][1:])
    _sum[i][1] = house[i][1] + min([_sum[i - 1][0], _sum[i - 1][2]])
    _sum[i][2] = house[i][2] + min(_sum[i - 1][:2])

print(min(_sum[-1]))