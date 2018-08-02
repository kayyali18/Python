# Hero's Inventory
# Demonstrates Lists

# create a list with some items and displat with a for loop

inventory = ["sword",
             "armor",
             "shield",
             "healing potion"]

print ("Your items:\t")
for item in inventory:
    print (item)
input ("Press Enter key to continue")

# get the length of items in inventory

print ("You have ", len(inventory), "in your inventory")

input ("\nPress Enter key to continue")

# test for membership using in operator

if "healing potion" in inventory:
    print ("\nYou will live to fight another day!")


# display one item through an index

index = int(input("\nEnter an index number for an item in inventory:\t"))

print ("In index, ", index, "is:\t", inventory[(index -1)])

## display a slice
start = int(input("\nEnter an index number to begin slice:\t"))
end = int(input("\nEnter an index number to end slice:\t"))

print ("inventory[", start, ":", end, "] is:", end = "")
print (inventory[start:end])
input ("\nPress Enter to continue")

## concatenate two lists

chest = ["gold", "gems"]

print ("You find a chest which contains:\t")
print (chest)
print ("\nYou add the contents of the chest to your inventory")
inventory += chest
print ("\nYour inventory is now:")
print (inventory)

# assign by index

print ("\nYou trade your sword for a crossbow")
inventory [0] = "crossbow"
print ("\nYour inventory is now:\t", end = "")
print (inventory)

input ("\nPress Enter key to exit")

# assign by slice

print ("You trade gold and gems for an orb of python learning")
inventory [4:6] = ["orb of python learning"]
print ("\nYour inventory s now:\t")
print (inventory)

input ("\nPress Enter to continue")

# delete an element

print ("\nIn a great battle, your shield is destroyed.")
del inventory [2]
print ("\nYour inventory is now:\t", end = "")
print (inventory)

input ("\nPress Enter key to exit")


print ("\nYou stumbled across some robbers, they stole your armour and \
healing potion")
del inventory [1:3]
print ("\nYour inventory is now:\t")
print (inventory)

input ("\nPress Enter key to exit")

