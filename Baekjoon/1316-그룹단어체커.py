n = int(input())
count = 0

for i in range(n):
    word = input()

    prev = word[0]
    group = []
    flag = True
    for c in word:
        if c in group:
            flag = False
            break
        if c != prev:
            group.append(prev)
            prev = c

    if flag:
        count += 1

print(count)