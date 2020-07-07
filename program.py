import random

def insertBoard(letter,pos):
    Board[pos] = letter

def  isFree(pos):
    if board[pos] == ' ':
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
    print("| " + b[7] + " | " + b[8] + " | " + b[9] + " |");
    print("+---+---+---+")
    print("| " + b[4] + " | " + b[5] + " | " + b[6] + " |");
    print("+---+---+---+")
    print("| " + b[1] + " | " + b[2] + " | " + b[3] + " |");
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
    print("Yet to think...")
