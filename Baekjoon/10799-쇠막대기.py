import sys

pipe = str(sys.stdin.readline()).strip()
piece = 0
stack = []

for i, p in enumerate(pipe):
    if p == "(":
        stack.append(p)
    else:
        if pipe[i - 1] == '(':
            piece += len(stack) - 1
        else:
            piece += 1
        stack.pop()

print(piece)
