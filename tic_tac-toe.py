# Creating a python game "Tic Tac Toe"

# Creating a board
board=[" - ",  " - ", " - ",
       " - ", " - ",  " - ",
       " - ", " - ", " - "]

# Displaying the board by definig a Function
def dispaly_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# Player "X" or "O
current_palyer=" X "

# Winner For Now
winner =None

# Boolean Value for the Game flow
game_going =True

#Handling the game turn
def handle_game():
    position = int(input("Enter a Number from 1-9: "))-1

    board[position] = current_palyer

    dispaly_board()

def check_game_over():
    # Checking for the row
    check_row()
    # Checking for the column
    #check_column()
    # Checking for the diagonals
    #check_diagonal()

# Checking for the row
def  check_row():
    global winner,game_going
    # First Row
    row_1 = board[0] == board[1] == board[2] != " - "
    # Second Row
    row_2 = board[3] == board[4] == board[5] != " - "
    # Third Row
    row_3 = board[6] == board[7] == board[8] != " - "
    if row_1:
        winner = board[0]
        # Ending the while Loop
        game_going = False
        return winner,game_going
    elif row_2:
        winner = board[3]
        # Ending the while Loop
        game_going = False
        return winner, game_going
    elif row_3:
        winner = board[6]
        # Ending the while Loop
        game_going = False
        return winner, game_going




# Defining a Function for Playing game
def play_game():

    # Displaying a  the Game Board
    dispaly_board()

    while game_going:
        #Handling the game turn
        handle_game()

        # Checking the winner or ending the game by tie up the match
        check_game_over()

        # Change the player
        #flip_palyer()

    # Winner Or Tie Up
    if winner == " X "  or winner ==" O ":
        print(winner, "Won.")
    else:
        print("Match Tie.")


# Calling the Play_Game Function
play_game()
