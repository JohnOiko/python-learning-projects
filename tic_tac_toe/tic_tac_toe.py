row_count = 3
column_count = 3
board = [[' ' for column in range(column_count)] for row in range(row_count)]


# print the current state of the board
def print_board():
    i = 0
    row_separator = f"{('-' * 5 + '+') * (column_count - 1)}{'-' * 5}"
    print(f"-{row_separator}-")
    for row in board:
        print("|", end="")
        for element in row:
            print(2 * " " + element + 2 * " ", end="|")
        if i == row_count - 1:
            print(f"\n-{row_separator}-")
        else:
            print(f"\n|{row_separator}|")
        i += 1


def input_move(player_symbol):
    print(f"{'First' if player_symbol == 'O' else 'Second'} player's turn ({player_symbol}) - input the row and "
          f"column of your next move.")
    x = input("Row: ")
    y = input("Column: ")
    print()
    while not x.isdigit() or not y.isdigit() or not 0 <= int(x) <= row_count - 1 or not 0 <= int(y) <= column_count - 1 \
            or board[int(x)][int(y)] != " ":
        print("Input a valid row and column for your next move.")
        x = input("Row (0 - 2): ")
        y = input("Column (0 - 2): ")
        print()
    return int(x), int(y)


def check_row_winner(player_symbol):
    for row in board:
        symbol_counter = 0
        for element in row:
            if element == player_symbol:
                symbol_counter += 1
                if symbol_counter == 3:
                    return True
    return False


def check_column_winner(player_symbol):
    for i in range(3):
        symbol_counter = 0
        for row in board:
            if row[i] == player_symbol:
                symbol_counter += 1
                if symbol_counter == 3:
                    return True
    return False


def check_main_diagonal_winner(player_symbol):
    symbol_counter = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == j and board[i][j] == player_symbol:
                symbol_counter += 1
                if symbol_counter == 3:
                    return True
    return False


def check_secondary_diagonal_winner(player_symbol):
    symbol_counter = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j == len(board[i]) - 1 and board[i][j] == player_symbol:
                symbol_counter += 1
                if symbol_counter == 3:
                    return True
    return False


def check_winner(player_symbol):
    if check_row_winner(player_symbol) or check_column_winner(player_symbol) \
            or check_main_diagonal_winner(player_symbol) or check_secondary_diagonal_winner(player_symbol):
        return True
    return False


def main():
    # initialize counters, winner and end flag
    player_symbol = 'X'
    turn_counter = 0
    winner = 0
    end_game = False

    while not end_game:

        print_board()
        print()

        # swap current player
        if player_symbol == 'X':
            player_symbol = 'O'
        else:
            player_symbol = 'X'

        turn_counter += 1

        # read the player's next move
        x, y = input_move(player_symbol)

        # update board with the player's move
        board[x][y] = player_symbol

        # increment turn counter and end game if there is a draw
        if turn_counter == 9:
            winner = '0'
            end_game = True

        # check if the current player has won
        if check_winner(player_symbol):
            winner = player_symbol
            end_game = True

    # print the final state of the board
    print_board()
    print()

    # if there is a winner print the according message, else print that there is a tie
    if winner != '0':
        print(f"Winner is the {'first' if winner == 'O' else 'second'} player ({winner}) after {turn_counter} turns!")
    else:
        print(f"We have a draw after {turn_counter} turns!")


main()
