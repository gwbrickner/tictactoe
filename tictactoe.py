# CMPSC 132 Final Project'
# Graeson Brickner
# I worked on this project alone and with no help from outside resources/persons

class Board:
    def __init__(self, xName, oName):
        self.board = [[0 for x in range(3)] for x in range(3)]
        self.symKey = {0: " ",
                       1: "O",
                       2: "X"}
        
        self.xKey = {"A": 0,
                     "B": 1,
                     "C": 2}
        
        self.xName = xName
        self.oName = oName

    def makeMove(self, symbol, x, y):
        x = self.xKey[x]
        if self.board[y][x] == 0:
            self.board[y][x] = symbol
            return True
        
        return False
    
    def validate(self, x, y):
        try:
            y = int(y)

        except:
            return False
        
        if x in self.xKey and y in range(3):
            return True
        
        return False
        
    @property
    def boardToStr(self):
        boardString = "  A B C\n"
        for y, row in enumerate(self.board):
            boardString += str(y) + " "
            for x, column in enumerate(row):
                boardString += self.symKey[column]
                if x != 2:
                    boardString += "|"
            if y != 2:
                boardString += "\n  -----\n"
            
        return boardString
    
    @property
    def won(self):
        # horizontal check
        for row in self.board:
            if row[0] == row[1] == row[2] != 0:
                if row[0] == 1:
                    return "o"

                else:
                    return "x"
        
        # vert check
        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != 0:
                if self.board[0][column] == 1:
                    return "o"

                else:
                    return "x"
                
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            if self.board[0][0] == 1:
                return "o"
            
            else:
                return "x"
        
        if self.board[2][0] == self.board[1][1] == self.board[0][2] != 0:
            if self.board[2][0] == 1:
                return "o"
            
            else:
                return "x"
        
        filledSquares = 0

        for y in range(3):
            for x in range(3):
                if self.board[y][x] != 0:
                    filledSquares += 1
        
        if filledSquares == 9:
            return "draw"

        return False

def checkWin(board):
    won = board.won
    if won == "x":
        print("Player 1, you win! Congratulations!")
    
    elif won == "o":
        print("Player 2, you win! Congratulations!")

    elif won == "draw":
        print("It's a draw!")

    else:
        return None
    
    print("If you would like to play again, press 'y' and then enter, otherwise, just press enter!")
    playAgain = input("Play again? ")

    if playAgain.strip().lower() == "y":
        return True
    
    else:
        return False
    
def main():
    print("Welcome to Tic-Tac-Toe!")
    xName = input("Player 1, please type your name and press enter: ")
    oName = input("Player 2, please type your name and press enter: ")

    board = Board(xName, oName)

    playing = True
    won = False
    currentPlayerNum = 1
    currentPlayerSymbol = 2

    while playing:
        print(board.boardToStr)
        choosing = True
        while choosing:
            xMove = input(f"Player {currentPlayerNum}, please input your move (e.g. B2): ").strip().upper()

            if len(xMove) == 2:
                validFlag = board.validate(xMove[0], xMove[1])

                if validFlag == True:
                    moveFlag = board.makeMove(currentPlayerSymbol, xMove[0], int(xMove[1]))

                    if moveFlag == True:
                        choosing = False

                        if currentPlayerNum == 1:
                            currentPlayerNum = 2
                            currentPlayerSymbol = 1
                        
                        else:
                            currentPlayerNum = 1
                            currentPlayerSymbol = 2
                    
                    else:
                        print("There is already an X/O at that square.")

                else:
                    print("Invalid character in move.")
            
            else:
                print("Invalid length of move.")
        
        winFlag = checkWin(board)
        if winFlag == True:
            board = Board(xName, oName)
            continue
            
        elif winFlag == False:
            playing = False
            continue
        
if __name__ == "__main__":
    main()