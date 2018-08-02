## Chapter 5
#
## Character Creator Program

print ("Welcome to the Character Creator Program. \n\
You have a pool of 30 point to use, that you can add to different attributes.\n\
Use these points wisely.")

input ("Press Enter to start")

## Menu to pick choices from
choice = None

# Create variable for available points
points = 30

# Dictionary of attributes and available starting points
attributes = {"Strength" : 0,
              "Health" : 0,
              "Wisdom" : 0,
              "Dexterity" : 0
              }

## While loop to go through menu choices

while choice != "0":
     print (
    """
    0 - Exit
    1 - Check available points
    2 - Add points to an attribute
    3 - See available attributes
    4 - Adjust attribute points
    5 - Check current attribute points

    """
    )

     choice = input ("Choice:\t")
     print ()

    # View amount of points available
     if choice == "1":
        print (points)

    # See attributes
     elif choice == "2":
        where = input ("Which attribute would you like to add to?:\t")
        
        if where not in attributes:
            print ("\nThe attribute you put in, isn't in the list. Check the \n\
                choices to see available attributes")
        else:
            add = int(input("\nHow many points would you like to add?:\t"))
            if (points - add) < 0:
                print ("You don't have that many points")
            else:
                attributes[where] += add
                points -= add
                print ("\nA value of", add, "point have been added to", where)

    # list all available attributes

     elif choice == "3":
        for keys in attributes:
            print (keys)


    # remove points from attribute

     elif choice == "4":
        where = input ("\nWhich attribute would you like to remove from?:\t")
        if where in attributes:
            add = int(input("\nHow many points would you like to remove?:\t"))
            if (attributes[where] - add) < 0:
                print ("You don't have that many points")
            else:
                points += add
                attributes[where] -= add
                print ("\nA value of", add, "has been removed from", where)
        else:
            print ("\nThat attribute isn't in the list, check the choices \n\
                available to see attributes.")

    # shows all attributes and corresponding points
     elif choice == "5":
         for key in attributes:
             print (key, attributes.get(key))
     else:
        print ("\nYour choice is invalid.")

print ("\nThank you for playing!")
input ("\nPress Enter to exit")


## choice 5 was this until, through some critical thinking I was able to fix it:
## where = input("\nWhich attribute would you like to check?:\t")
##         if where in attributes:
##             print (attributes.get(where))
##         else:
##             print ("\nThe attribute you picked doesn't exist. Check the \n\
##                choices available to see attributes")
##            
##            
##            
