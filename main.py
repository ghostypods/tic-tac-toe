def create_board():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board


def display_board(board):
    row_count = 0
    for row in board:
        print(" | ".join(row))
        if row_count < 2:
            print('- + - + -')
        row_count += 1


def player_move(board, player):
    while True:
        try:
            move = input(f"Player {player}, make your move (row and column): ")
            row, col = map(int, move.split())
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This spot is taken, try again.")
        except (ValueError, IndexError):
            print("Invalid value. Please enter numbers in between 0 and 2 (e.g. 0 2)")


def check_winner(board, player):
    for row in board:
        if all(r == player for r in row):
            return True

    for col in range(len(board)):
        if all(board[row][col] == player for row in range(len(board))):
            return True

    if all(board[i][i] == player for i in range(len(board))):
        return True

    if all(board[i][2-i] == player for i in range(len(board))):
        return True


def check_draw(board):
    if all(cell != " " for row in board for cell in row):
        return True


def main():
    board = create_board()
    current_player = "X"

    game_is_on = True
    while game_is_on:
        display_board(board)
        player_move(board, current_player)

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins")
            game_is_on = False

        if check_draw(board):
            display_board(board)
            print("It's a draw")
            game_is_on = False

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
