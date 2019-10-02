for i in range(int(input())):
    H, W, N = map(int, input().split(" "))
    floor = str(N % H) if N % H != 0 else str(H)
    room_Num = str(N // H + 1).zfill(2) if N % H != 0 else str(N // H).zfill(2)
    print(floor + room_Num)

