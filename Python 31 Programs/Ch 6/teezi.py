def ask_yes_or_no (question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y", "n"): ##if response is not y or n run code
        response = input(question).lower()
    return question


answer = ask_yes_or_no ("\nPlease enter 'y' or 'n':\t")

print ("Thanks for entering:\t", answer)
