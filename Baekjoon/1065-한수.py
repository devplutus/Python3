def find(n):
    if len(str(n)) < 3:
        return 1
    else:
        n = str(n)
        gap = int(n[1]) - int(n[0])
        for i in range(2, len(n)):
            new_gap = int(n[i]) - int(n[i-1])
            if gap != new_gap:
                return 0

        return 1
            

n = int(input())
_sum = 0
for i in range(1, n+1):
    _sum += find(i)

print(_sum)
