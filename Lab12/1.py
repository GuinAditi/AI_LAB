import math

# ----------------------------
# Print Board
# ----------------------------
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# ----------------------------
# Check Winner
# ----------------------------
def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

# ----------------------------
# Check if Moves Left
# ----------------------------
def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

# ----------------------------
# Evaluate Board
# ----------------------------
def evaluate(board):
    winner = check_winner(board)
    if winner == "X":   # AI
        return 10
    elif winner == "O": # Human
        return -10
    return 0

# ----------------------------
# Alpha-Beta Pruning
# ----------------------------
def alpha_beta(board, depth, is_max, alpha, beta):
    score = evaluate(board)

    # Terminal states
    if score == 10 or score == -10:
        return score

    if not is_moves_left(board):
        return 0

    if is_max:  # AI's move
        best = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    val = alpha_beta(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "

                    best = max(best, val)
                    alpha = max(alpha, best)

                    # PRUNING
                    if beta <= alpha:
                        break

        return best

    else:  # Human's move
        best = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    val = alpha_beta(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "

                    best = min(best, val)
                    beta = min(beta, best)

                    # PRUNING
                    if beta <= alpha:
                        break

        return best

# ----------------------------
# Find Best Move for AI
# ----------------------------
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = alpha_beta(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

# ----------------------------
# MAIN GAME
# ----------------------------
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Tic Tac Toe (You = O, AI = X)\n")

    while True:
        print_board(board)

        # Human move
        row, col = map(int, input("Enter your move (row col): ").split())
        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue

        board[row][col] = "O"

        if check_winner(board) == "O":
            print_board(board)
            print("You win!")
            break

        if not is_moves_left(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = "X"

        print("\nAI played:\n")

        if check_winner(board) == "X":
            print_board(board)
            print("AI wins!")
            break

        if not is_moves_left(board):
            print_board(board)
            print("It's a draw!")
            break


# Run the game
play_game()