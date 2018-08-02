## Hero's Inventory 2.0
## Demonstrates Tuples

# create a tuple with some items and display with a for loop
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")
print ("Your items:\t")
for item in inventory:
    print (item)

input ("\nPress Enter key to continue")

# get the length of a tuple

print ("You have", len(inventory), "items in your possession.")

input ("\nPress Enter key to continue")

## in Operator is used to test for membership - whether \n
## in a string or a tuple

# test for membership with in

if "healing potion" in inventory:
    print ("You will live to fight another day!")

## The condition (if "healing potion" in inventory) tests to see if \
    # the entire string "healing potion" is an element in inventory. \
    # Since it is, the message "You will live to fight another day" is displayed

## Indexing in tuples works like indexing in strings

# display one item through an index

index = int(input("\nEnter the index number for an item in inventory:\t"))
print ("At index", index, "is", inventory[index])

# display a slice
start = int(input("\nEnter the index number to begin a slice:\t"))
finish = int(input("\nEnter the index number to end the slice:\t"))
print ("inventory[", start, ":", finish, "] is", end = " ")
print (inventory[start:finish])

input ("\nPress Enter key to continue")

## Tuples are immutable you can't change them
# But like strings you can create new tuples from existing ones
# Of course through concatenation


# Concatenate two tuples

chest = ("gold", "gems")
print ("You find a chest, it contains:")
print (chest)

print ("You add the contents of the chest to your inventory")
inventory += chest
print ("Your inventory is now:")
print (inventory)

index = int(input("Enter an index number for an item in inventory:\t"))
print ("At index", index, "is", inventory[index])
input ("\nPress Enter key to exit")




