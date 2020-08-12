# Creating a python game "Tic Tac Toe"

# Creating a board
board=["-", "-", "-",
       "-", "-", "-",
       "-", "-", "-"]

# Displaying the board by definig a Function
def dispaly_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# Defining a Function for Playing game
def play_game():

    # Displaying a the Game Board
    dispaly_board()

    # Handling the game turn
    Handle_turn()

    # Checking the winner or ending the game by tie up the match
    check_winner()

    # Change the player
    flip_palyer()

