n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

_sum = [arr[0] for i in range(3)]

for i in range(3):
    if i == 0:
        _continue