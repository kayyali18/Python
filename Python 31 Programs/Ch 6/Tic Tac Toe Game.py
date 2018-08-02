## Tic-Tac-Toe
## Plays the game of tic-tac-toe against a human opponent

# global CONSTANTS

# X represents X
X = "X"
# O represents O
O = "O"
# EMPTY represents an empty square on the board
EMPTY = " "
# TIE represents a tie game
TIE = "TIE"
# NUM_SQUARES is the number of squares on the board
NUM_SQUARES = 9

# Define a function to display instructions
def display_instruct ():
    # function documentatino string
    """Display game instructions."""

    print(

"""

Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
This will be a showdown between your human brain and my silicon processor.

You will make your move known by entering a number, 0 - 8. The number
will correspond to the board position as illustrated:


\t\t0 | 1 | 2
\t\t---------
\t\t3 | 4 | 5
\t\t---------
\t\t6 | 7 | 8

Prepare yourself, human. The ultimate battle is about to begin. \n

"""

)

## Define a function to ask for yes or no
    # Receives a question
    # Returns either a "y" or "n"
def ask_yes_no (question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input (question).lower()
    return response

## Define a function that ask for a number within a range
    # Receives a question, low number, and a high number
    # Returns a number in range from low to high
def ask_number(question, low, high, step):
    """Ask for a number within range"""
    response = None
    step = 1
    while response not in range (low, high, step):
        response = int(input(question))
    return response

## Define a function to determine who goes first
    # Returns the computer's piece and t3he human's piece
    # This function utilises the ask_yes_no function
    # Functions can call other functions
def pieces ():
    """Determine if player or computer goes first"""
    go_first = ask_yes_no("\aDo you want to go first? (y/n):\t")
    if go_first == "y":
        print ("\nThen take the first move. You will need it!")
        human = X
        computer = O
    else:
        print ("\nYour bravery will be your undoing..... I will go first.")
        computer = X
        human = O
    return computer, human

## Defines a function to create an empty board
    # Returns a board
def new_board ():
    """Create new game board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append (EMPTY)
    return board

## Defines a function to display the board
    # Receives a board
def display_board(board):
    """Display game board on screen"""
    print ("\n\t", board [0], "|", board [1], "|", board [2])
    print ("\t", "---------")
    print ("\n\t", board [3], "|", board [4], "|", board [5])
    print ("\t", "---------")
    print ("\n\t", board [6], "|", board [7], "|", board [8])
    
## Defines a function to be used by other functions to return a list of legal moves
    # Used by human_move() to make sure player chooses a valid move
    # Used by computer_move() so computer can consider only valid moves
    # Works by looping over the board checking for empty squares
    # If a square is empty, it is added to the legal moves list
    # Then it returns the legal moves list
def legal_moves(board):
    """Create a list of legal moves"""
    moves = []
    for square in range (NUM_SQUARES):
        if board [square] == EMPTY:
            moves.append (square)
    return moves

## Defines a function to determine if a game is a win or TIE
    # Defines a constant (WAYS_TO_WIN) which has all 8 ways one can win
    # All the ways to win are in an immutable tuple
    # Use a for loop to go through each possible way a player can win
    # If statement checks to see if one checks out and no square is empty in the sequence
    # Receives a board
    # Returns a piece, "TIE", or None
def winner (board):
    """Determines the game winner"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board [row[0]] == board [row[1]] == board [row[2]] != EMPTY:
            winner = board [row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

# Define a function that asks for a human move and checks to see if legal
    # Set variable to legal_moves(board)
    # Set variable move to None to work with later in function
    # Function gets list of legal moves
    # Then continues to ask for a square number until response is legal
    # Receives a board and the human's piece
    # Returns the human's move
def human_move (board, human):
    """Get human move"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("\nWhere will you move? (0 - 8):\t", 0, NUM_SQUARES, 1)
        if move not in legal:
            print ("\a\n That square is already occupied foolish human. Choose another.\n")
    print ("Fine...")
    return move

def computer_move (board, computer, human):
    """Make a computer move"""
    # make a copy to work with since this function will be changing list
    board = board [:]
    # the best positions for the computer to have in order
    BEST_MOVES = (4, 0 , 2, 6, 8, 1, 3, 5, 7)

    print ("\nI shall take the square number", end = " ")
    # if computer can win, take that move
    for move in legal_moves(board):
        board [move] = computer
        if winner (board) == computer:
            print (move)
            return move
    # done checking this move, undo it
        board [move] = EMPTY
    # if human can win, block that move
    for move in legal_moves(board):
        board [move] = human
        if winner (board) == human:
            print (move)
            return move
    # donce checking this move, undo it
        board [move] = EMPTY
    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves (board):
            print (move)
            return move

# Define a function that switches turns
    # Switches turns based on current turn
    # Receives a piece
    # Returns a piece
def next_turn (turn):
    """Switch turns"""
    if turn == X:
        return O
    else:
        return X

# Defines a function to congratulate winner based on result
    # Congratulates winner or declares a TIE
    # Receives the winning piece, the computer's piece, and the human's piece
def congrat_winner(the_winner, computer, human):
    """Congratulate the winner"""
    if the_winner != TIE:
        print (the_winner, "\awon!\n")
    else:
        print ("It's a tie!\n\a")

    if the_winner == computer:
        print ("As I predicted, human, I am triumphant once more.  \n" \
               "Proof that computers are superior to humans in all regards.\a")

    elif the_winner == human:
        print ("No, no! It cannot be! Somehow you tricked me, human. \n" \
               "But never again! I, the computer, so swear it!\a")

    elif the_winner == TIE:
        print ("You were the most lucky, human, and somehow managed to tie me.  \n" \
               "Celebrate today... for this is the best you will ever achieve! \a")

        
## This is where I define the main() function
    # It is best to encapsulate the main() function as well
    # Rather than keep it global
def main():
    # display intructions
    display_instruct()
    # determine who goes first
    computer, human = pieces ()
    turn = X
    # create empty board
    board = new_board ()
    # display the board
    display_board (board)

    # while nobody's won and it's not a tie
    while not winner (board):
        # if it's the humans turn
        # get human's move
        # update board with move
        if turn == human:
            move = human_move (board, human)
            board [move] = human
        # otherwise
        # calculate the computer's move
        # update the board with the move
        else:
            move = computer_move (board, computer, human)
            board [move] = computer
        # display the board
        display_board (board)
        # switch turns
        turn = next_turn (turn)

    # congratulate winner or declare tie
    the_winner = winner (board)
    congrat_winner (the_winner, computer, human)

# Now it's time to call the main () function
    # the next line calls the main function
    # in turn it calls all the other functions from the global level

# Start the program

main ()
input ("\a\nPress the Enter key to exit")

    


