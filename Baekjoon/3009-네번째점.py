x_dot = []
y_dot = []
for i in range(3):
    x,y = list(map(int, input().split(" ")))
    if x in x_dot:
        x_dot.remove(x)
    else:
        x_dot.append(x)
    if y in y_dot:
        y_dot.remove(y)
    else:
        y_dot.append(y)
print(x_dot[0], y_dot[0])
