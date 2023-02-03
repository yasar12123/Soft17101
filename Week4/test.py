def crossReference (input, list):
    if input in list:
        print(True)
    else:
        print(False)

winningMoves = [(1,2,3), (4,5,6), (7,8,9),
                (1,4,7), (2,5,8), (3,6,9),
                (1,5,9), (3,5,7)]

moves = [6,5,4]
moves.sort()
crossReference(moves, winningMoves)