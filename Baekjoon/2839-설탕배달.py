n = int(input())
a = []
for i in [3, 5]:
    for j in [3, 5]:
        if i != j:
            for x in range(1, (n // i + 1)):
                _value = []
                if (n - (i * x)) % j == 0:
                    _value.append(x)
                    _value.append((n - (i * x)) // j)
                    a.append(_value)

if a:
    print(min([sum(i) for i in a]))
else:
    print("-1")