import random

def insertBoard(letter,pos):
    Board[pos] = letter

def  isFree(pos):
    if board[pos] == ' ':
        return True

def isFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def isWinner(board, letter):
    return((board[1] and board[2] and board[3]) or
    (board[4] and board[5] and board[6]) or
    (board[7] and board[8] and board[9]) or
    (board[1] and board[4] and board[7]) or
    (board[2] and board[5] and board[8]) or
    (board[3] and board[6] and board[9]) or
    (board[1] and board[5] and board[9]) or
    (board[3] and board[5] and board[7]))

def printBoard():
    print("+---+---+---+")
    print("| " + b[7] + " | " + b[8] + " | " + b[9] + " |")
    print("+---+---+---+")
    print("| " + b[4] + " | " + b[5] + " | " + b[6] + " |")
    print("+---+---+---+")
    print("| " + b[1] + " | " + b[2] + " | " + b[3] + " |")
    print("+---+---+---+")

def playerMove():
    run = True
    while run:
        move = input("Please select a position place an X(1-9): ")
        try:
            move = move(int)
            if move > 0 and move < 10:
                if isFree(move):
                    insertBoard('X',move)
                else:
                    print("Position already occupied! Try again...")
            else:
                print("Choose a number within the grid(1-9)")
        except:
            print("Don't you know that you should enter a number? Poor fella")

def selectRandom(lis):
    length = len(lis)
    rtr = random.randRange(0,length)
    return rtr

def computerMove():

    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]

    move = 0
    for let in ['X', 'O']:
        if i in possibleMoves:
            boardCopy = board[:]
            if isWinner(boardCopy, let):
                move = let
                return move

    if 5 in possibleMoves:
        move = 5
        return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if cornersOpen > 0:
        move = selectRandom(cornersOpen)
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if edgesOpen > 0:
        move = selectRandom(edgesOpen)
        return move

board = [' ' for x in range(10)]

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("It takes god level talent to beat this AI. Better know the rules")
    printBoard()

    while not(isFree(board)):
        if not(isWinner(board,'O')):
            playerMove()
            printBoard()
        else:
            print('AI won! Get your brain tested')
            break
            if not(isWinner(board, 'X')):
                move = computerMove()
                if move == 0:
                    print("Game tied. Well played!")
                else:
                    insertBoard('X', move)
                    print('Computer inserted an X a pos: ', move)
                    printBoard()
            else:
                print("You won master! I surrender")
                break

    if isFull(board):
        print("Game tied... Well played!")

    main()
    while True:
        ans = input("Do you want to play again? (Y/N)")
        if ans == 'Yes' or ans == 'Y':
            board = [' ' for x in range(10)]
            main()
        else:
            break
