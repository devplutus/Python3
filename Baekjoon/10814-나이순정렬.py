n = int(input())
people = []
for i in range(n):
    human = input().split()
    people.append([int(human[0]), human[1]])

people.sort(key = lambda x:x[0])

for i in people:
    print(i[0], i[1])