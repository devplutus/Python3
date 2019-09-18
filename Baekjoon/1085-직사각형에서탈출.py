x,y,w,h = list(map(int, input().split(" ")))
x1 = w - x
y1 = h - y
arr = [x, y, x1, y1]
print(min(arr))