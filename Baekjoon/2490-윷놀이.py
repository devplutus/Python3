bars = ["A", "B", "C", "D"]
for i in range(3):
    turn = list(map(int, input().split())).count(0)
    if turn == 0:
        print("E")
    else:
        print(bars[turn - 1])


