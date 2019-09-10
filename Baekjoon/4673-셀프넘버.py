arr = {i : 0 for i in range(1, 10001)}

for i in arr:
    _sum = i

    for l in str(i):
        _sum += int(l)
    
    if _sum in arr:
        arr[_sum] += 1

for x in [i for i in arr if arr[i] == 0]:
    print(x)