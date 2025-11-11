""" Find Four - Lab 02
    Programmers: Sophia Pappous, Grace Zhao
    Date: 9/05/24"""

def main():
    full = False
    p1_win = False
    p2_win = False

    print("Welcome to Find Four!")
    print("---------------------")

    while True:

        # Row input and checking
        row = input("Enter height of board (rows): ")
        if row.lstrip('-').isdigit():
            row = int(row)
            if row < 4 :
                print("Error: height must be at least 4!")
                continue
            if row > 25 :
                print("Error: height can be at most 25!")
                continue
        else:
            print("Error: not a number!")
            continue

        while True:
            # Column input and checking... does not start until row is valid
            column = input("Enter width of board (columns): ")
            if column.lstrip('-').isdigit():
                column = int(column)
                if column < 4 :
                    print("Error: width must be at least 4!")
                    continue
                if column > 25 :
                    print("Error: width can be at most 25!")
                    continue
            else:
                print("Error: not a number!")
                continue

            # Starts the game by creating and printing the board
            board = get_initial_board(row, column)
            print_board(board)
            print("Player 1: x\n"
                  "Player 2: o\n")

            # Continues the game if it is not over
            # Asks player 1 to select a column, and gives an error if the input doesn't work
            while full != True and p1_win != True and p2_win != True:
                p1_input = input("Player 1 - Select a Column: ")
                if p1_input.lstrip('-').isdigit():
                    p1_input = int(p1_input)
                    if p1_input > column - 1 or p1_input < 0:
                        print("Error: no such column!")
                        continue
                    if board[row-1][p1_input] != ".":
                        print("Error: column is full!")
                        continue
                else:
                    print("Error: not a number!")
                    continue

                # Puts the chip in, and ensures that the game can continue
                p1_row = insert_chip(board, p1_input, "x")
                board[p1_row][p1_input] = "x"
                print_board(board)
                full = is_board_full(board)
                p1_win = is_win_state("x", board, p1_row, p1_input )

                if p1_win:
                    print("Player 1 won the game!")
                if full:
                    print("Draw game! Players tied.")

                # Continues the game if it is not over
                # Asks player 2 to select a column, and gives an error if the input doesn't work
                while full != True and p1_win != True and p2_win != True:
                    p2_input = input("Player 2 - Select a Column: ")
                    if p2_input.lstrip('-').isdigit():
                        p2_input = int(p2_input)
                        if p2_input > column - 1 or p2_input < 0:
                            print("Error: no such column!")
                            continue
                        if board[row - 1][p2_input] != ".":
                            print("Error: column is full!")
                            continue
                    else:
                        print("Error: not a number!")
                        continue

                    # Puts the chip in, and ensures that the game can continue
                    p2_row = insert_chip(board, p2_input, "o")
                    board[p2_row][p2_input] = "o"
                    print_board(board)
                    full = is_board_full(board)
                    p2_win = is_win_state("o", board, p2_row, p2_input)

                    if p2_win:
                        print("Player 2 won the game!")
                    if full:
                        print("Draw game! Players tied.")
                    break

            break
        break



# creating the initial board with user input of columns and rows
def get_initial_board(rows: int, columns: int):
    board = [["." for _ in range(columns)] for _ in range(rows)]
    return board

# prints the current board when called
def print_board(board: list[list[str]]):
    # print top border
    print(" ", end='')
    for i in range(len(board[0]) *2 -1):
        print("_", end='')
    print("")
    # print middle (with empty spaces to play)
    for j in range(len(board)-1, -1, -1):
        print("|", end='')
        for k in range(len(board[0]) - 1):
            print(board[j][k], "", end='')
        print(board[j][len(board[0])-1], end = "|\n")
    # print end border
    print(" ", end='')
    for l in range(len(board[0]) * 2 - 1):
        print("-", end='')
    print("\n")

# returns the row in which a chip should be put in for the designated player
def insert_chip(board: list[list[str]], column: int, chip: str):
    row = -1
    # Checks if the space is empty or not for each row
    for i in range(len(board)):
        if board[i][column] == ".":
            board[i][column] = chip
            row = i
            break
    return row

# checks if the player that just went won
def is_win_state(chip: str, board: list[list[str]], row: int, column: int):
    count = 0
    for i in range(len(board)):
        if board[i][column] == chip:
            count += 1
        else:
            count = 0
        if count == 4:
            return True
    for j in range(len(board[0])):
        if board[row][j] == chip:
            count += 1
        else:
            count = 0
        if count == 4:
            return True
    return False

# checks if the board is full
def is_board_full(board: list[list[str]]):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                return False
    return True

if __name__ == "__main__":
    main()