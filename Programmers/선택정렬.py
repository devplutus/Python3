array = [14, 4, 8, 23, 11, 5, 3, 2, 4, 9]

for i in range(0, len(array)):

    min = array[i]
    index = i

    for j in range(i, len(array)):
        if(min > array[j]):
            min = array[j]
            index = j
    
    temp = array[i]
    array[i] = array[index]
    array[index] = temp

print(array)
