## Trivia Challenge Game
## Trivia Game that reads a plain text file

## import system module [sys] to use sys.exit()
import sys, pickle, shelve

# def function to open file
# receives a file name and mode such as ("r", "w", "w+", etc.)
def open_file (file_name, mode):
    """Open a file"""
    try:
        the_file = open(file_name, mode)
    # Create exception to handle IOError such as file doesn't exist
    except IOError as error:
        print ("Unable to open the file", file_name, "Ending program. \n", error)
        input ("Press Enter key to exit")
        sys.exit()
    # Otherwise, if all clear - return var the_file
    else:
        return the_file
    

# define a function to print next line
## receives a file object and returns the next line of text from file object
### Parameter used is (the_file) from open_file function
def next_line (the_file):
    """Return the next line from the trivia file, formatted"""
    line = the_file.readline()
    # replace all instances of "/" with newline \n
    line = line.replace ("/", "\n")
    return line

# define a function to read a block of lines for a question
## takes file object, returns 4 strings and a list of strings
### returns strings for - category, question, correct answer, and explanation
#### returns a list as well for possible answers to question
def next_block (the_file):
    """Return the next block of data from the trivia file"""
    # category is = to next_line fx with parameter the_file
    category = next_line (the_file)

    # same goes for question
    question = next_line(the_file)
    # create an empty list to add possible answers to
    answers = []
    for i in range (4):
        # iterate through range of 4
        ## append the lines to answers
        ### call function next_line with parameter the_file returned from open_file fx
        answers.append(next_line(the_file))
    # create variable correct
    ## make it equal to next_line fx with parameter the_file returned from fx 
    correct = next_line(the_file)
    points = next_line (the_file)
    if correct:
        correct = correct [0]
    # create var explanation = to next_line fx with the_file parameter returned from fx
    explanation = next_line(the_file)
    # return all variables created
    return category, question, answers, correct, points, explanation


# def function to welcome the player and print title of episode
def welcome (title):
    """Welcome the player, get his/her name"""
    print ("\t\tWelcome to Trivia Challenge \n")
    print ("\t\t", title, "\n")

# define a fx to keep track of scores
def high_scores (score):
    question = input ("Would you like to add your score to the high scores list? [y/n]:\t")
    if question == "y":
        username = input ("Enter your username:\t")
        # create empty dictionary
        user_list = []
        # update dictionary with username as key and score as value
        user_list.append(username)
        user_list.append (":\t")
        user_list.append (str(score))
        user_list.append ("\n")
        # set var to = to the file with the high scores
        # make it open the file
        text_file = open ("high_scores.txt", "a+")
        text_file.writelines (user_list)
        text_file.close()
        # dump the user dict to pickle_data i.e. high_scores
        text_file = open ("high_scores.txt", "r")
        print (text_file.read ())

# open pickle to show high scores
# def a fx to show scores in pickled file (high_scores)
##def show_scores():
##    # new method of opening a pickle and assigning to a var
##        with open("high_scores.txt", "r") as file:
##            # handling exceptions
##            try:
##                #while something is in the file
##                while True:
##                    # yield from the pickle
##                    print (file.read())
##            # create an exception for an end of file error
##            # once a readline  ()  hits the end of file
##            # this exception runs
##            except EOFError:
##                print ("That's all the scores")
##        file.close ()
##        
        
# create main () function to hold the main loop
## first we set up the game by opening the file
### second, we get the title of the episode (the first line of file)
### third, welcome the player
#### finally set the player's score to 0
def main ():
    # set var trivia_file = to the_file returned by fx open_file()
    trivia_file = open_file("mytrivia.txt", "r")
    # set var title = to what is returned by next_line fx with trivia_file as parameter
    title = next_line (trivia_file)
    # call welcome fx with title parameter
    welcome (title)
    # set score to 0
    score = 0
    # read first block of lines for first question into variables
    # start while loop to continue to ask until category is not empty string
    # if category is an empty string, the loop will end
    # ask a question by printing the category, the question, and possible answers

    # get first block
    # set multiple variables in order from which I set them
    # to next_block fx with parameter of trivia_file
    category, question, answers, correct, points, explanation = next_block (trivia_file)
    while category:
        # ask a question
        print (category)
        print (question)
        for i in range (4):
            print ("\t", i + 1, "-", answers [i])
        # get answer
        answer = input ("What's your answer?:\t")
        # check answer
        if answer == correct:
            print ("\nRight!", end = " ")
            score += int(points)
        else:
            print ("\nWrong!", end = " ")
        print (explanation)
        print ("Score:", score, "\n")
        print ("Possible amount of points from question:\t", points, end = "\n\n")
        # get next block of questions by calling for next_block fx
        category, question, answers, correct, points, explanation = next_block (trivia_file)
    # after the loop ends
    # close the file as good practice
    trivia_file.close ()

    print ("\nThat was the last question!")
    print ("\n Your final score is", score)
    high_scores (score)
    # call show scores fx with a for loop
    # print all items in the fx
##    show_scores ()

# call main () to start game
main ()
input ("Press Enter to exit")

    
    
        
    
    

        

