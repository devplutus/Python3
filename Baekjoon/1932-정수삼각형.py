n = int(input())

triangle = []

for i in range(n):
    triangle.append(list(map(int, input().split())))

_sum = triangle[-1]

for i in range(1, n):
    for x in range(len(triangle[i])):
        if x == 0:
            triangle[i][x] += triangle[i-1][0]
        else:
            triangle[i][x] += max(triangle[i-1][x-1:x+1])
    
print(max(triangle[-1]))

