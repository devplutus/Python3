array = [1, 7, 5, 10, 8, 9, 2, 3, 7, 8, 2, 5]

for i in range(0, len(array)):
    for j in range(0, len(array) - i - 1):
        if(array[j] > array[j + 1]):
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp

print(array)

n = 50
num = 0

for i in range(0, n):
    for j in range(0, n):
        num += 1
    for j in range(0, n):
        num += 1

print(num)
