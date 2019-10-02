import queue, sys

a = queue.Queue()
for i in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        a.put(cmd[1])
    elif cmd[0] == "pop":
        print(-1) if a.empty() else print(a.get())
    elif cmd[0] == "size":
        print(a.qsize())
    elif cmd[0] == "empty":
        print(1) if a.empty() else print(0)
    elif cmd[0] == "front":
        print(-1) if a.empty() else print(a.queue[0])
    elif cmd[0] == "back":
        print(-1) if a.empty() else print(a.queue[-1])
    