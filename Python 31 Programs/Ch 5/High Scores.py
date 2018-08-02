# High Scores
## Demonstrates list methods

scores = []
choice = None

while choice != "0":

    print (
        """
High Scores

1 - Show Scores
2 - Add a Score
3 - Delete a Score
4 - Sort Scores
"""
        )
    choice = input ("Choice:\t")
    print ()

    # exit
    if choice == "0":
        print ("Good-bye!")
    # list high score table
    elif choice == "1":
        print ("High Scores")
        for score in scores:
            print (score)
    elif choice == "2":
        score = int(input("What score did you get?:\t"))
        scores.append(score)
    elif choice == "3":
        score = int(input("Remove which score?:\t"))
        if score in scores:
            scores.remove(score)
        else:
            print(score, " isn't in the high scores list")
    #sort scores
    elif choice == "4":
        scores.sort(reverse = True)

    # some unknown choice
    else:
        print ("Sorry, but", choice, "is invalid!")


input ("\nPress Enter to exit")

        
        
        
                    
        
