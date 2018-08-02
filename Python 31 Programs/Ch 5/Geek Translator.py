## Geek Translator
# Demonstrates Dictionaries

geek = {"404": "clueless. From the web error message 404, meaning \
page not found. ",
        "Googling": "searching the Internet for background information \
on a person. ",
        "Keyboard Plaque": "the collection of debris found in computer \
keyboards.",
        "Link Rot": "the process by which a web page link becomes  \
obsolete.",
        "Percussive Maintenance": "the act of striking an electronic \
device to make it work",
        "Uninstalled": "being fired. Especially popular during the \
dot-bomb era.",
        "Dancing Baloney": "animated graphics and other visual effects \
that have no substantive value, often used by web designers to impress \
clients"}

choice = None

while choice != "0":
    print(
        """
    Geek Translator

    0 - Quit
    1 - Look Up a Term
    2 - Add a Geek Term
    3 - Redefine a Geek Term
    4 - Delete a Geek Term
    5 - Show all entries
    """
        )

    choice = input("Choice:\t")
    print()

    # exit
    if choice == "0":
        print ("\nGood-bye!")
    # get a definition
    elif choice == "1":
        term = input("\nWhat term do you want to look up?:\t")
        if term in geek:
            print (geek.get(term))
        else:
            print ("\nSorry man, not in here!")
    # add a definition

    elif choice == "2":
        term = input("\nWhat is the term you want to add?:\t")
        
        if term in geek:
            print ("\nWe already have that and it means:\n", geek.get(term))
        else:
            definition = input("\nDefine it please:\t")
            geek[term] = definition
            print ("\n")
            print (term, "has been added to the dictionary")

    # redefine a term
    
    elif choice == "3":
        term = input("What is the term you want to redefine?:\t")
        if term not in geek:
            print ("That term doesn't exist, try adding one instead")
        else:
            definition = input("Your new definition:\t")
            geek[term] = definition
            print ("\n", term, "has been redifined")

    # delete a term-definition pair
    elif choice == ("4"):
        term = input("Which term would you like to delete?:\t")
        if term in geek:
            del geek[term]
            print ("\n", term, "has been removed from the dictionary!")
        else:
            print("\n", term, "doesn't exist in geek dictionary")
    # list dictionary keys
    elif choice == "5":
        for keys in geek:
            print (keys)
        
    # some unknown choice
    else:
        print ("Sorry, your choice", choice, "is invalid. Try again!")

input ("\nPress Enter key to exit")

## Dictionary Methods

# get a value from key, with optional default triggered
print (geek.get("Not a key", "If key doesn't exist, this is returned [default]"))
input ("Press Enter")
# print all dictionary keys
print (geek.keys())
input ("Press Enter")
# print all dictionary values
print (geek.values())
input ("Press Enter")
# print all of dictionary items. Keys and values
print (geek.items())
input ("Press Enter if you're satisfied")
    

    
        
        
