from sys import stdin

def merge_Sort(arr):
    if len(arr) == 1:
        return [arr[0]]

    mid = len(arr) // 2
    l_arr = arr[:mid]
    r_arr = arr[mid:]

    if len(l_arr) != 1:
        l_arr = merge_Sort(arr[:mid])
    if len(r_arr) != 1:
        r_arr = merge_Sort(arr[mid:])

    temp = []
    l = 0
    r = 0
    while l < len(l_arr) and r < len(r_arr):
        if l_arr[l] > r_arr[r]:
            temp.append(r_arr[r])
            r += 1
        else:
            temp.append(l_arr[l])
            l += 1

    if l != len(l_arr):
        temp += l_arr[l:]
    else:
        temp += r_arr[r:]

    return temp


n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(int(stdin.readline()))
for i in merge_Sort(arr):
    print(i)

"""
import time
arr = [3, 2, 45, 6, 4, 1, 23]

a = time.time()
print(sorted(arr))
print(time.time() - a)
a = time.time()
print(merge_Sort(arr1))
print(time.time() - a)

기존 Python Sort = 0.0009975433349609375
Merge Sort = 0.003988742828369141
"""