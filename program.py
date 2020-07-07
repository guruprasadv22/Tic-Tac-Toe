
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
