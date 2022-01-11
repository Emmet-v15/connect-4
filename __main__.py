
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
        print("   ", end='')
        for i in range(len(self.board[0])):
            print(str(i+1) + " ", end='')
        print()
        i = 0
        for y in self.board:
            i += 1
            print(str(i) + "| ", end='')
            for x in y:
                print(x + " ", end='')
            print()

    def getFreeSlot(self, col):
        if col < len(self.board[0]):
            return self.freespaces[col]

    def claimSlot(self, row, col, playerid):
        self.board[row][col] = playerId
        if self.freespaces == 0:
            return
        self.freespaces[col] -= 1

    def checkForWinner(self, row, col):
        for i in self.board[col]:
            print(self.board[])
        return None


if __name__ == "__main__":
    board = Board(9, 9)

    board.printBoard()

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
                col = int(col)
                row = board.getFreeSlot(col)
                if row != "full":
                    break
            board.claimSlot(row, col, playerId)
            if board.checkForWinner(row, col):
                winner = playerId
