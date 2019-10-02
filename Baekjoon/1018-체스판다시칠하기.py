def check_Board(color, check, N, M):
    if color == "B":
        if N % 2 == 0:
            board = ["W", "B"]
        else:
            board = ["B", "W"]
        
    elif color == "W":
        if N % 2 == 0:
            board = ["B", "W"]
        else:
            board = ["W", "B"]

    if (M % 2 == 0 and check == board[0]) or (M % 2 == 1 and check == board[1]):
        return 1
    else:
        return 0

N, M = map(int, input().split())

board = []
black = []
white = []
for i in range(N):
    board.append(list(input()))


for x in range(N - 7):
    for y in range(M - 7):
        st_Black = 0
        st_White = 0
        for i in range(x, x + 8):
            for j in range(y, y + 8):
                st_Black += check_Board("B", board[i][j], i, j)
                st_White += check_Board("W", board[i][j], i, j)

        black.append(st_Black)
        white.append(st_White)


print(min([min(black), min(white)]))
            