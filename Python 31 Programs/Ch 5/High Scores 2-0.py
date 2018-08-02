# High Scores 2.0

# Demonstrates nested sequences

scores = []

choice = None

while choice != 0:
    print(
    """
    High Scores 2.0

    0 - Quit
    1 - List Scores
    2 - Add a Score
    """
          )

    choice = input ("Choice:\t")
    print ()

    # exit

    if choice == "0":
        print ("Good-bye!")
    elif choice == "1":
        print ("High Scores")
        print ("NAME\t\tSCORE")
        for entry in scores:
            score, name = entry
            print (name,"\t",score)
    # add a score      
    elif choice == "2":
        score = int(input("\nEnter your score:\t"))
        name = input("\nEnter your name:\t")
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse = True)
        scores = scores[:5] # keep only top 5 scores

    # some unknown choice
    else:
        print ("Sorry, your choice", choice, "is invalid!")

input ("\nPress Enter to exit")

    
