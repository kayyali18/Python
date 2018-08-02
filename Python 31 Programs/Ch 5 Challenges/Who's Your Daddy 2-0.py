## Who's Your Daddy
## Ch 5 Challenges

family = {"Ahmad" : "Bassam",
          "Bassam" : "Muhammad",
          "Zulfa" : "Asem",
          "Asem" : "Hilmi",
          "Tom" : "Dick",
          "Dick" : "Harry",
          "Brooke" : "Robert",
          "Robert" : "TJ",
          "Bader" : "Mahmood",
          "Mahmood" : "Nijm"
          }

choice = None

while choice != "0":

    choice = input (
        """
    0 - Exit
    1 - Add a family tree
    2 - Replace a family tree
    3 - Delete a family tree
    4 - Show all families

    """
        )
# Exit
    if choice == "0":
        print ("Good-bye!")
    # Add a family tree
    
    elif choice == "1":
        son = input ("What is the name of the son?:\t")
        father = input ("What is the name of the father?:\t")
        if son in family:
            print ("We can't do that, not that advanced yet")
        else:
            family[son] = father
        addition = input ("Would you like to add a grandfather?:\t")
        if addition == "Yes":
            grandfather = input ("What is his name?:\t")
            family[father] = grandfather
        elif addition == "No":
            print ("Cool Beans!")
    #Replace a family tree
            
    elif choice == "2":
        replace = input ("Would you like to replace a son, father, grandfather or all?:\t")
        ## Replace a son only
        if replace == "Son":
            son = input ("Who would you like to replace?:\t")
            if son in family:
                replace_son = input ("Who would you like to replace it with:\t")
                family[replace_son] = family.pop(son)
                print (son, "has been replace with", replace_son)
            else:
                print ("Sorry,", son, "isn't in the list")
        ## Replace a father only
        elif replace == "Father":
            son = input ("Who's dad would you like to replace?:\t")
            if son in family:
                replace_father = input ("Who would you like to replace him with:\t")
                x = family.get (son)
                family[son] = replace_father
                family[replace_father] = family.pop(x)
                print (x, "has been replaced with", replace_father)
            else:
                print ("Sorry", son, "isn't in the list")
        ## Replace a grandfather only
        elif replace == "Grandfather":
            son = input ("Who's grandfather?:\t")
            if son in family:
                replace_grandfather = input ("Who would you like to replace him with:\t")
                father = family.get (son)
                family[father] = replace_grandfather
                print (son, "'s Grandfather has been replaced with", replace_grandfather)
            else:
                print ("Sorry", son, "isn't in the list")
        ## Replace a whole family tree
        elif replace == "All":
            son = input ("Who's family would you like to replace?:\t")
            if son in family:
                replace_son = input ("Who would you like to replace him with?:\t")
                replace_father = input ("His father's name?:\t")
                replace_grandfather = input ("His grandfather's?:\t")
                # get  value of son i.e. (father)
                x = family.get (son)
                # get value of father i.e (grandfather)
                x_2 = family.get (x)
                # delete element of father : grandfather
                family.pop(x, None)
                # create new element key = replace son & value = replace father
                family[replace_son] = replace_father
                # delete element of son : father
                family.pop(son, None)
                # create a new element key = replace father & value = replace granfather
                family[replace_father] = replace_grandfather
                print ("\n",son, "has been replaced with", replace_son)
                print ("\n", x, "has been replaced with", replace_father)
                print ("\nAnd", x_2, "has been replaced with", replace_grandfather)
            else:
                print (son, "isn't in the list")

     ## Delete a family tree           
    elif choice == "3":
        son = input ("Who's family should I delete?:\t")
        if son in family:
            x = family.get (son)
            family.pop(x, None)
            family.pop(son, None)
            print ("\n", son, "'s family has been deleted")
        else:
            print ("\n", son, "isn't in the list")

    ## Display all father son pairs
    elif choice == "4":
        for key in family:
            print (key, "\t", family.get(key))

    ## some other choice
    else:
        print ("\nYour choice is invalid")

input ("\nPress Enter key to exit")
