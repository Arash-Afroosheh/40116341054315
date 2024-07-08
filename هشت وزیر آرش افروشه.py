#Arash Afroosheh
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_queen(board, row, n):
    if row >= n:
        return True
    
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queen(board, row + 1, n):
                return True
            board[row] = -1
    return False

def print_solution(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def eight_queens():
    n = 8
    board = [-1] * n
    if solve_queen(board, 0, n):
        print_solution(board)
    else:
        print("No solution exists.")

eight_queens()