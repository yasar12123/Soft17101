
def printBoard(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def crossReference (input, list):
    if input in list:
        print(True)
    else:
        print(False)

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
boardPlacements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
winningMoves = [[1,2,3], [4,5,6], [7,8,9],
                [1,4,7], [2,5,8], [3,6,9],
                [1,5,9], [3,5,7]]

userPlacement = 0
userPiece = " "
computerPiece = " "
userMoves = []
computerMoves = []
winnerDecided = False

#Ask user to select a piece
userPiece = input("Do you want to be 0 or X")
if userPiece == "0":
    computerPiece == "x"
else:
    computerPiece = "0"

#main code to loop around moves untill winner is determined
while winnerDecided is False:
    printBoard(boardPlacements)
    userPlacement = int(input("Which square do you want to place your move in")) - 1
    board[userPlacement] = userPiece
    userMoves.insert(0, userPlacement+1)
    boardPlacements[userPlacement] = " "
    printBoard(board)

    if userMoves in winningMoves:
        print("You have won")
        winnerDecided = True
    elif computerMoves in winningMoves:
        print("You have lost")
        winnerDecided = True
    print(userMoves)


#print(userPlacement)
#print(userPiece)
#print(computerPiece)
