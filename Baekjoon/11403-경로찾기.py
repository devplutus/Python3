n = int(input())

arr = [["0" for j in range(n)] for i in range(n)]

for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j] == 1:
            arr[i][j] = "1"
            arr[j][i] = "1"
            arr[j][j] = "1"
print("--------------------")
for a in arr:
    _str = ""
    for j in a:
        _str += "{} ".format(j)
    print(_str)
