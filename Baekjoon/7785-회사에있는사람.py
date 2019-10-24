import sys

n = int(sys.stdin.readline().strip())
people = {}

for i in range(n):
    name, state = sys.stdin.readline().strip().split()
    if state == "enter":
        people[name] = 1
    else:
        del people[name]

remains = [k for k, v in people.items()]
if len(remains):
    remains.sort()

    for p in reversed(remains):
        print(p)

"""
5
Artem enter
baha enter
Baha enter
Askar enter
Baha leave
"""
