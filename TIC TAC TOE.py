def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, mark):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == mark for cell in row):
            return True
    for col in range(3):
        if all(row[col] == mark for row in board):
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_move():
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter values between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter numerical values.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        row, col = get_move()
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("The game is a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell is already occupied. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
