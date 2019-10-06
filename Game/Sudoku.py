import random, time

"""
참조 : https://www.101computing.net/sudoku-generator-algorithm/
"""

class Sudoku:

    def __init__(self, row = 9, col = 9, way = 0):
        self.row = row
        self.col = col
        self.board = [[0 for i in range(col)] for i in range(row)]
        self.numbers = [i for i in range(1, 10)]
        # 0 : Magic, 1 : Latin
        self.way = way

    def create(self):

        if self.way == 0:
            self.create_Diagonal()

        for i in range(0, self.row * self.col):
            r, c = i // 9, i % 9
            if self.board[r][c] == 0:
                random.shuffle(self.numbers)
                for n in self.numbers:
                    if self.vertify(n, r, c):
                        self.board[r][c] = n
                        if self.all_check():
                            return True
                        else:
                            if self.create():
                                return True
                break
        self.board[r][c] = 0
    
    def create_Diagonal(self):
        for i in range(0, self.row * self.col):
            r, c = i // 9, i % 9
            if (r == c or r + c == 8) and self.board[r][c] == 0:
                random.shuffle(self.numbers)
                for n in self.numbers:
                    if self.vertify(n, r, c):
                        self.board[r][c] = n
                        if self.diagonal_Check():
                            return True
                        else:
                            if self.create_Diagonal():
                                return True
                break
        self.board[r][c] = 0

    def vertify(self, n, r, c):

         # 가로
        if n in self.board[r]:
            return False

        # 세로
        if n in [b[c] for b in self.board]:
            return False

        if self.way == 0:
            # 왼쪽 대각선
            if r == c and n in [self.board[i][i] for i in range(9)]:
                return False
            
            # 오른쪽 대각선
            if r + c == 8 and n in [self.board[i][8 - i] for i in range(9)]:
                return False
        
        # 3X3 블록
        cell = ()
        for i in range(3):
            cell += tuple(self.board[(r // 3) * 3 + i][(c // 3) * 3:(c // 3 + 1) * 3])
        if n in cell:
            return False
        
        return True

    def all_check(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return False
        return True
    
    def diagonal_Check(self):
        for r in range(9):
            for c in range(9):
                if (r == c or r + c == 8) and self.board[r][c] == 0:
                    return False
        return True

    def show(self):
        if self.way == 0:
            print("- 완전방진 -")
        else:
            print("- 라틴방진 -")

        print("-------------------------")
        for i, b in enumerate(self.board):
            if i // 3 > 0 and i % 3 == 0:
                print("-------------------------")
            print("| {} {} {} | {} {} {} | {} {} {} |".format(b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8]))
        print("-------------------------")


for i in range(2):
    s = Sudoku(way=i)
    prev = time.time()
    s.create()
    s.show()
    print("생성 시간 : %0.3f s\n" % float(time.time() - prev))