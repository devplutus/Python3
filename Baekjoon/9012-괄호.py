import sys
for i in range(int(sys.stdin.readline())):
    stack = []
    s = sys.stdin.readline()
    for i in range(len(s) - 1):
        if s[i] == "(":
            stack.append("(")
        elif len(stack) and s[i] == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(s[i])
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
