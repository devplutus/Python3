n = int(input())
f0 = 0
f1 = 1
f2 = f1 + f0
s = 2
while s < n:
    f0 = f1
    f1 = f2
    f2 = f1 + f0
    s += 1
print(f2)