n = int(input())
arr = []
count = 1
num = 666
while True:
    if str(num).count("666") >= 1:
        if count == n:
            print(num)
            break
        count += 1
    
    num += 1