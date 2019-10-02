n = int(input())
_sum = 1
count = 1
while True:
    if n <= _sum:
        for i in range(1, count + 1):
            if n == _sum:
                if count % 2 == 0:
                    print("{}/{}".format(count - i + 1, i))
                else:
                    print("{}/{}".format(i, count - i + 1))
                    
                break
            _sum -= 1
        break

    count += 1
    _sum += count