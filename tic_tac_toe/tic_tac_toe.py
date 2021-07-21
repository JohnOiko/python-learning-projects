board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
symbols = ("O", "X")

# initialize counters, winner and end flag
current_player = 2
turn_counter = 0
winner = 0
end_game = False

while not end_game:

    # print the current state of the board
    i = 0
    print("------+-----+------")
    for row in board:
        print("|", end="")
        for element in row:
            print(2 * " " + element + 2 * " ", end="|")
        if i == 2:
            print("\n------+-----+------")
        else:
            print("\n|-----+-----+-----|")
        i += 1
    print()

    # swap current player
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1

    turn_counter += 1

    # read the player's next move
    print("Player " + str(current_player) + "'s turn (" + symbols[current_player - 1] + "s) - input the row and column "
                                                                                        "of your next move."
          )
    x = int(input("Row: "))
    y = int(input("Column: "))
    print()
    while x < 0 or x > 2 or y < 0 or y > 2 or board[x][y] != " ":
        print("Player " + str(current_player) + "'s turn (" + symbols[current_player - 1] + "s) - input a valid row "
                                                                                            "and column for your next "
                                                                                            "move.")
        x = int(input("Row (0 - 2): "))
        y = int(input("Column (0 - 2): "))
        print()

    # update board with the player's move
    board[x][y] = symbols[current_player - 1]

    # increment turn counter and end game if there is a draw
    if turn_counter == 9:
        winner = 0
        end_game = True

    symbol_counter = 0

    # check rows for a winner
    for row in board:
        symbol_counter = 0
        for element in row:
            if element == symbols[current_player - 1]:
                symbol_counter += 1
        if symbol_counter == 3:
            winner = current_player
            end_game = True

    # check columns for a winner
    for i in range(3):
        symbol_counter = 0
        for row in board:
            if row[i] == symbols[current_player - 1]:
                symbol_counter += 1
        if symbol_counter == 3:
            winner = current_player
            end_game = True

    # check the main diagonal for a winner
    symbol_counter = 0
    for i in range(3):
        for j in range(3):
            if i == j and board[i][j] == symbols[current_player - 1]:
                symbol_counter += 1
    if symbol_counter == 3:
        winner = current_player
        end_game = True

    # check the secondary diagonal for a winner
    symbol_counter = 0
    for i in range(3):
        for j in range(3):
            if i + j == 2 and board[i][j] == symbols[current_player - 1]:
                symbol_counter += 1
    if symbol_counter == 3:
        winner = current_player
        end_game = True

# print the final state of the board
i = 0
print("------+-----+------")
for row in board:
    print("|", end="")
    for element in row:
        print(2 * " " + element + 2 * " ", end="|")
    if i == 2:
        print("\n------+-----+------")
    else:
        print("\n|-----+-----+-----|")
    i += 1
print()

# if there is a winner print the according message, else print that there is a tie
if winner != 0:
    print("Winner is player " + str(winner) + " (" + str(symbols[winner - 1]) + "s) after " + str(
        turn_counter) + " turns!")
else:
    print("We have a tie after " + str(turn_counter) + " turns!")
