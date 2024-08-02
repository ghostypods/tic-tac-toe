def create_board():
    board = [[" ", " ", " ",],
             [" ", " ", " ",],
             [" ", " ", " ",]]

    return board


def display_board(board):
    row_count = 0
    for row in board:
        print(" | ".join(row))

        if row_count < 2:
            print("- + - + -")

        row_count += 1


def player_move(board, player):
    while True:
        try:
            move = input(f"Player {player}, select your move (row and column): ")
            row, col = map(int, move.split())
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This spot is taken")
        except (ValueError, IndexError):
            print("Invalid move. Please select a row and column between 0 and 2")


def check_winner(board, player):
    for row in board:
        if all(r == player for r in row):
            return True

    for col in board:
        if all(c == player for c in col):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True


def check_draw(board):
    if all(cell != " " for row in board for cell in row):
        return True


def main():
    board = create_board()
    current_player = 'X'

    gamie_is_on = True
    while gamie_is_on:
        display_board(board)
        player_move(board, current_player)

        if check_winner(board, current_player):
            print(f"Player {current_player} has won!")
            gamie_is_on = False

        if check_draw(board):
            print(f"Its a draw!")
            gamie_is_on = False

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
