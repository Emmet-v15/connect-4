class Board():

    def __init__(self, row, col):
        self.board = []
        for i in range(row):
            _col = []
            for i in range(col):
                _col.append(".")
            self.board.append(_col)

        self.freespaces = []
        for i in range(col):
            self.freespaces.append(row-1)

    def printBoard(self):
        boardStr = "\n"*1 + "   "
        for i in range(len(self.board[0])):
            boardStr += str(i+1) + " "
        boardStr += "\n"
        i = 0
        for y in self.board:
            i += 1
            boardStr += str(i) + "| "
            for x in y:
                boardStr += x + " "
            boardStr += "\n"
        print(boardStr)

    def getFreeSlot(self, col):
        if self.freespaces[col] < 0:
            return None
        return self.freespaces[col]

    def claimSlot(self, row, col, playerId):
        if self.freespaces[col] < 0:
            return
        self.board[row][col] = playerId
        self.freespaces[col] -= 1

    def checkForWinner(self, row, col):
        buff = [None, 0]
        for y in self.board:
            if y[col] == buff[0] and y[col] != ".":
                buff[1] += 1
                if buff[1] >= 3:
                    return True
            else:
                buff = [y[col], 0]
        buff = [None, 0]

        for x in self.board[row]:
            if x == buff[0] and x != ".":
                buff[1] += 1
                if buff[1] >= 3:
                    return True
            else:
                buff = [x, 0]

        x, y = row, col
        while x != 0 and y != 0:
            x-=1
            y-=1

        buff = [None, 0]
        while x <= len(self.board)-1 and y <= len(self.board[0])-1:
            if self.board[x][y] == buff[0] and self.board[x][y] != ".":
                buff[1] += 1
                if buff[1] >= 3:
                    return True
            else:
                buff = [self.board[x][y], 0]
            x+=1
            y+=1
        
        x, y = row, col
        while x != len(self.board)-1 and y != 0:
            x+=1
            y-=1
        buff = [None, 0]
        while x != 0 and y <= len(self.board[0])-1:
            print(self.board[x][y])
            if self.board[x][y] == buff[0] and self.board[x][y] != ".":
                print(self.board[x][y])
                buff[1] += 1
                if buff[1] >= 3:
                    return True
            else:
                buff = [self.board[x][y], 0]
            x-=1
            y+=1


        return False



if __name__ == "__main__":
    board = Board(9, 9)

    players = ["R", "G"]
    winner = None

    while not winner:
        for playerId in players:
            print("Player", playerId + "'s Turn to slot a disc:")
            board.printBoard()
            col = 0
            row = 0
            while True:
                while not col:
                    col = input("SELECT COLUMN (1-6)#> ")
                col = int(col)-1
                row = board.getFreeSlot(col)
                if row != None:
                    break
                print("Column full, retry")
                col = None
            board.claimSlot(row, col, playerId)
            if board.checkForWinner(row, col):
                winner = playerId
                break
    board.printBoard()
    print(playerId, "won!")
