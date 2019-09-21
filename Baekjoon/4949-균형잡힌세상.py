import sys

sign = {
    "]" : "[",
    ")" : "("
}

while True:
    s = sys.stdin.readline()
    if s == ".\n":
        break
    else:
        stack = []
        for i in range(len(s)-1):
            if s[i] in sign.values():
                stack.append(s[i])
            elif s[i] in sign:
                if len(stack) and stack[-1] == sign[s[i]]:
                    stack.pop()
                else:
                    stack.append(s[i])

        if len(stack):
            print("no")
        else:
            print("yes")