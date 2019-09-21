a = input()
b = input()
numbers = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]

for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        if a[j - 1] == b[i - 1]:
            numbers[i][j] = numbers[i - 1][j - 1] + 1
        else:
            if numbers[i - 1][j] > numbers[i][j - 1]:
                numbers[i][j] = numbers[i - 1][j]
            else:
                numbers[i][j] = numbers[i][j - 1]

print(numbers[-1][-1])

"""
a = ACAYKP
b = CAPCAK
    0   A   C   A   Y   K   P
-------------------------------
0 | 0   0   0   0   0   0   0
C | 0   0   1   1   1   1   1
A | 0   1   1   2   2   2   2
P | 0   1   1   2   2   2   3
C | 0   1   2   2   2   2   3
A | 0   1   2   3   3   3   3
K | 0   1   2   3   3   4   4

"""