n = int(input())

for i in range(n):
    _str = ""
    line = input().split(" ")
    for j in line[1]:
        _str += j * int(line[0])
    print(_str)
