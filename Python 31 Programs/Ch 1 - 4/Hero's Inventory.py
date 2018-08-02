## Hero's Inventory
## Demonstrates Tuple Creation

# create an empty tuple
inventory = ()

# treat the tuple as a condition
if not inventory:
    print ("You are empty-handed.")

input ("\n\nPress Enter to exit")

# create a tuple with some items
inventory = ("sword",
             "armor",
             "shield",
             "healing potion",
             "dragon's fire")
# print the tuple
print ("\nThe tuple inventory is:\t")
print (inventory)

# print each element in the tuple
print ("\nYour items:\t")
for item in inventory:
    print (item)
print (len(inventory))
input ("\n\nPress Enter key to exit")
