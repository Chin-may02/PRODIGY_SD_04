def print_(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def find(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def valid(board, num, row, col):
    if num in board[row]:
        return False
    if num in (board[i][col] for i in range(9)):
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board):
    empty = find(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if valid(board, num, row, col):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False

def get():
    board = []
    print("Enter the Sudoku puzzle (use 0 for empty cells):")
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
                if len(row) != 9 or any(n < 0 or n > 9 for n in row):
                    raise ValueError
                board.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter 9 numbers separated by spaces (0 for empty cells).")
    return board

sudoku_board = get()  

if solve(sudoku_board):
    print("Sudoku solved successfully!")
    print_(sudoku_board)
else:
    print("No solution exists.")
