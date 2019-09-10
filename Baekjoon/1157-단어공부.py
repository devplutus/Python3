from collections import Counter

c = dict(Counter(input().lower()))
_max = max(c.values())
arr = [i for i in c if c[i] == _max]

if len(arr) > 1:
    print("?")
else:
    print(arr[0].upper())

