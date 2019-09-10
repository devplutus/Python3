arr = list(map(int, input().split(" ")))
Total = arr[0]
profit = arr[2] - arr[1]
if profit <= 0:
    print("-1")
else:
    print((Total // profit) + 1)

