import sys
n = int(sys.stdin.readline())
stack = []
pop = []
compare = []
sign = []
for i in range(n):
    compare.append(int(sys.stdin.readline()))

index = 0

for i in range(1, n+1):
    stack.append(i)
    sign.append("+")
    while len(stack) and compare[index] == stack[-1]:
        pop.append(stack.pop())
        sign.append("-")
        index += 1

if pop == compare:
    for i in sign:
        print(i)
else:
    print("NO")