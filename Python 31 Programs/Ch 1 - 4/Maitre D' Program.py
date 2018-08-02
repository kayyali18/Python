##Maitre D' Program
## This program demonstrates how to treat values as True or False
## Values such as string or integers return false if
## They are empty (strings) or 0 (integers)

print("Welcome to Cafe Du Paris.")
print("It seems we are quite full this evening.\n")

##Create variable money, and make money the condition.
##If int(Input) is 0 == False else == True
##It could be translated to "if there is money...."
##Side note: Negative values still result in True

money = int(input("How many dollars do you slip the Maitre D'? "))
## The code of line below means
## If money != 0 
if money:
    print("Ah, I am reminded of a table. Right this way Miseour.")
else:
    print("Please, sit. It may be a while.")

input ("Press Enter key to exit.")
