n = int(input())
info = []
rank = []
[info.append(list(map(int, input().split()))) for i in range(n)]

for i in range(len(info)):
    k = 0
    for j in range(len(info)):
        if i != j and info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            k += 1

    rank.append(str(k + 1))

print(" ".join(rank))