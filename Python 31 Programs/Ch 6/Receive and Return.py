## Receive and Return
## Demonstrates parameters and return values

# define function to display a message

def display (message):
    print (message)

# define function to give number 5

def give_me_five ():
    five = 5
    return (five)

# define function that only returns result if answer is y or no

def ask_yes_or_no (question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input (question).lower()
    return response


# main code using the functions

display ("Here's a message for you \n")

##number = give_me_five ()
print ("Here's what I got from give_me_five():\t", give_me_five())

answer = ask_yes_or_no ("\nPlease enter 'y' or 'n':\t")
print ("Thanks for entering:\t", answer)

