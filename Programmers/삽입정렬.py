array = [8, 4, 7, 1, 11, 5, 3, 2, 4, 9]

for i in range(0, len(array)):

    for j in range(i, 0, -1):
        if(array[j] < array[j-1]):
            temp = array[j]
            array[j] = array[j - 1]
            array[j - 1] = temp

        else:
            break


print(array)