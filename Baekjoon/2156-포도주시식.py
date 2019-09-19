arr = []
for i in range(int(input())):
    arr.append(int(input()))

_sum = [0 for i in range(len(arr))]
_sum [0] = arr[0]

for i in range(1, len(arr)):
    compare = []
    if i >= 3:
        compare.append(arr[i] + arr[i - 1] + _sum[i - 3])
    else:
        compare.append(arr[i] + arr[i - 1])
    compare.append(_sum[i - 1])
    compare.append(arr[i] + _sum[i - 2])

    _sum[i] = max(compare)

print(_sum[-1])


"""
6   10  13  9   8   1
            s
        
        1. 이전 + 지금 먹은 경우 연속 되는 시점 뒤 부터의 합으로 계산
        2. 이전만 먹은 경우 그대로 계산
        3. 지금만 먹은 경우 전 전 합으로 계산
"""