stack = []
for i in range(int(input())):
    n = int(input())
    stack.append(n) if n != 0 else stack.pop()
print(sum(stack))