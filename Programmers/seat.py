C = 7
R = 6

init_C = 0
init_R = 0
max_C = C - 1
max_R = R - 1

index = 1

# 위로 R 좌우로 C

array = [[0 for x in range(R)] for y in range(C)]

while(True):

    for r in range(init_R, max_R+1):
        array[init_C][r] = index
        index += 1
    
    init_C += 1

    for c in range(init_C, max_C+1):
        array[c][max_R] = index
        index += 1

    max_R -= 1

    for r in range(max_R, init_R-1, -1):
        array[max_C][r] = index
        index += 1

    max_C -= 1

    for c in range(max_C, init_C-1, -1):
        array[c][init_R] = index
        index += 1

    init_R += 1

    
    if(index > C * R): break

for i in array:
    print(i)
