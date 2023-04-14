"""
Homework 3 - Exercise 3
Name: Darion Badillo
Date: 02/23/2023
Description of your program: This program is a game of tic-tac-toe. Although functional, it does not pick a winner.
"""


# Displays the rules of the game
def print_rules():
    print("Tic-Tac-Toe")
    print("___________________________________________________________________________________________________________")
    print("Rules:")
    print("___________________________________________________________________________________________________________")
    print("First person to get three consecutive spots on the board wins\n"
          "If the board is full, the game will end in a draw.\n"
          "Note: User will make their move by typing an abbreviated form of the position of the board.\n"
          "For example, \"ul\" equates to upper left and the board position will be flipped to either an 'X' or an 'O',"
          "\ndepending on the player.")


# Displays the names of the moves the user must enter in order to play the game. This prints before every move 
def print_legend():
    print("___________________________________________________________________________________________________________")
    print("\nMove Legend")
    print("Upper left: ul        Upper middle: um        Upper right: ur\n"
          "Middle left: ml       Middle middle: mm       Middle right: mr\n"
          "Lower left: ll        Lower middle: lm        Lower right: lr")
    print("___________________________________________________________________________________________________________")
    print()


# Takes inventory dictionary and prints a neatly formatted inventory
def print_board(game_board):
    counter = 0

    print("\nCurrent Board")
    print("___________________________________________________________________________________________________________")

    for k, v in game_board.items():
        print(f'| {v} ', end="|")
        counter += 1
        if counter == 3:
            print()
            counter = 0


# Flips the cells of the board and replaces empty cells with either an X or an O
def play_game(game_board, player_move, user):

    # Updates board depending on the player's move
    if user == 1:
        game_board[player_move] = "X"
    elif user == 2:
        game_board[player_move] = "O"

    # Returns new board
    return game_board


# main
# game board dictionary
board = {"ul": "_", "um": "_", "ur": "_",
         "ml": "_", "mm": "_", "mr": "_",
         "ll": "_", "lm": "_", "lr": "_"}

# Empty list to hold all already played moves
played_moves = []
game_over = False
count = int(1)

# Prints rules of tic-tac-toe
print_rules()
# Loops until game_over is given and will exit loop
while not game_over:
    print_board(board)
    print_legend()

    # Determines player turn
    if count % 2 == 0:
        player = 2
    else:
        player = 1

    # Asks user for to make a choice of adding an item, deleting an item, or printing current inventory
    move = input(f'\nPlayer {player}: Make your move\n')

    # Checks if move is valid move in existing dictionary
    if move in board.keys():

        # checks to see if this is the first move of the game to add move to the list of played moves and then plays it
        if not played_moves:
            played_moves.append(move)
            count += 1
            board = play_game(board, move, player)

        # Checks if the move has already been made to make sure the game doesn't overwrite an existing move
        if move not in played_moves:

            # Adds the move to played moves list and then plays it
            played_moves.append(move)
            count += 1
            board = play_game(board, move, player)

        # If move has already been made, then this will display instead of playing the move
        else:
            print("Invalid move\nTry again")

    # If the move is not in the scope of the game board, then the move will not play
    else:
        print("Invalid move")

    # Sets bool value to true to exit loop and then displays the final board
    if count == 11:

        print("No more possible moves."
              "\nGame over")
        game_over = True
        print("\nFinal Board\n")
        print_board(board)

print("\nHave a good day!")
