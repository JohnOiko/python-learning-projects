import random
from random import seed, randrange, choice
from datetime import datetime
seed(datetime.now())

row_count = 3
column_count = 3
board = [[' ' for column in range(column_count)] for row in range(row_count)]


# print the current state of the board
def print_board():
    i = 0
    row_separator = f"{('-' * 5 + '+') * (column_count - 1)}{'-' * 5}"
    print(f"row -{row_separator}-")
    for row in board:
        print(f" {i}  |", end="")
        for element in row:
            print(2 * " " + element + 2 * " ", end="|")
        if i == row_count - 1:
            print(f"\n    -{row_separator}-")
        else:
            print(f"\n    |{row_separator}|")
        i += 1

    print(f"{' ' * 7}", end="")
    for i in range(column_count):
        print(f"{i}{' ' * 5 if i < column_count - 1 else ''}", end="")
    print(f"{' ' * 3}col")


def computer_moves(level):
    if level == 1:
        x = randrange(row_count)
        y = randrange(column_count)
        print(f"[{x}, {y}]")
        while board[x][y] != " ":
            x = randrange(0, row_count)
            y = randrange(0, column_count)

        print(f"The computer placed an O on the position [{x}, {y}]\n")
        return x, y

    elif level == 2:

        # check rows for near player victory
        for i in range(len(board)):
            x = y = -1
            symbol_counter = 0
            for j in range(len(board[i])):
                if board[i][j] == "X":
                    symbol_counter += 1
                elif board[i][j] == " ":
                    x, y = i, j
                if symbol_counter == 2 and x != -1:
                    print(f"The computer placed an O on the position [{x}, {y}]\n")
                    print("Source: row\n")
                    return x, y

        # check columns for near player victory
        for j in range(column_count):
            x = y = -1
            symbol_counter = 0
            for i in range(len(board)):
                if board[i][j] == "X":
                    symbol_counter += 1
                elif board[i][j] == " ":
                    x, y = i, j
                if symbol_counter == 2 and x != -1:
                    print(f"The computer placed an O on the position [{x}, {y}]\n")
                    print("Source:col\n")
                    return x, y

        # check main diagonal for near player victory
        x = y = -1
        symbol_counter = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i == j and board[i][j] == "X":
                    symbol_counter += 1
                elif i == j and board[i][j] == " ":
                    x, y = i, j
                if symbol_counter == 2 and x != -1:
                    print("Source: main diag\n")
                    print(f"The computer placed an O on the position [{x}, {y}]\n")
                    return x, y

        # check secondary diagonal for near player victory
        x = y = -1
        symbol_counter = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i + j == len(board[i]) - 1 and board[i][j] == "X":
                    symbol_counter += 1
                elif i + j == len(board[i]) - 1  and board[i][j] == " ":
                    x, y = i, j
                if symbol_counter == 2 and x != -1:
                    print(f"The computer placed an O on the position [{x}, {y}]\n")
                    print("Source: sec diag\n")
                    return x, y

        # check if the center of the board is empty
        if board[row_count // 2][column_count // 2] == " ":
            print(f"The computer placed an O on the position [{row_count // 2}, {column_count // 2}]\n")
            print("Source: center of board\n")
            return row_count // 2, column_count // 2

        # check if the corners of the board are empty
        empty_corners = []
        if board[0][0] == " ":
            empty_corners.append((0, 0))
        if board[0][column_count - 1] == " ":
            empty_corners.append((0, column_count - 1))
        if board[row_count - 1][column_count - 1] == " ":
            empty_corners.append((row_count - 1, column_count - 1))
        if board[row_count - 1][0] == " ":
            empty_corners.append((row_count - 1, 0))
        x, y = choice(empty_corners)
        print(f"The computer placed an O on the position [{x}, {y}]\n")
        print("Source: random corner\n")
        return x, y

        # check all positions that are in the middle of rows and columns
        empty_middles = []
        for i in range(row_count):
            if board[i][len(board[i]) // 2] == " ":
                empty_middles.append((i, len(board[i]) // 2))
        for j in range(column_count):
            if board[row_count // 2][j] == " ":
                empty_middles.append((row_count // 2, j))
        x, y = choice(empty_middles)
        print(f"The computer placed an O on the position [{x}, {y}]\n")
        print("Source: middle of row or col\n")
        return x, y

        # if no other move was possible, return a random available position
        x = randrange(row_count)
        y = randrange(column_count)
        print(f"[{x}, {y}]")
        while board[x][y] != " ":
            x = randrange(0, row_count)
            y = randrange(0, column_count)

        print(f"The computer placed an O on the position [{x}, {y}]\n")
        print("Source: random position\n")
        return x, y


def input_move(player_symbol):
    print(f"Your turn ({player_symbol}), input the row and "
          f"column of your next move.")
    x = input("Row: ")
    y = input("Column: ")
    print()
    while not x.isdigit() or not y.isdigit() or not 0 <= int(x) <= row_count - 1 or not 0 <= int(y) <= column_count - 1\
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
    for i in range(column_count):
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

    level = input("Give difficulty level: ")
    while level not in ["1", "2"]:
        level = input("Give difficulty level (1 or 2): ")
    level = int(level)

    # initialize counters, winner and end flag
    player_symbol = 'O'
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

        if player_symbol == 'X':
            # read the player's next move
            x, y = input_move(player_symbol)
        else:
            # save the computer's next random move
            x, y = computer_moves(level)

        # update board with the player's move
        board[x][y] = player_symbol

        # increment turn counter and end game if there is a draw
        if turn_counter == 9:
            winner = ''
            end_game = True

        # check if the current player has won
        if check_winner(player_symbol):
            winner = player_symbol
            end_game = True

    # print the final state of the board
    print_board()
    print()

    # if there is a winner print the according message, else print that there is a tie
    if winner == 'O':
        print(f"You lost after {turn_counter} turns.")
    elif winner == 'X':
        print(f"You won after {turn_counter} turns!")
    else:
        print(f"Draw after {turn_counter} turns!")


main()
