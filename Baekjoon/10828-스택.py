import sys
stack = []
for i in range(int(sys.stdin.readline())):
    arr = sys.stdin.readline().split()
    if arr[0] == "push":
        stack.append(arr[1])

    elif arr[0] == "pop":
        print(stack.pop()) if len(stack) else print(-1)

    elif arr[0] == "size":
        print(len(stack))

    elif arr[0] == "empty":
        print(0) if len(stack) else print(1)

    elif arr[0] == "top":
        print(stack[-1]) if len(stack) else print(-1)