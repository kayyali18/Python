## Backwards Word Printer or Backword printer ("I'm so funny ahaha")
## Take a message from user, print it out backwards

print ("Welcome user, for this program I will ask you to write a message \n\
and I will spit it out backwards for you.")
# Ask user for message to be reversed
message = input("Enter the message you'd like to be reversed:\n\t")

# Gets length of message so we can get the first(last position) letter of
## message

first_letter = -len(message)
#print (first_letter)
## position variable to be edited because last character (first position)
### is -1
position = -1
## empty variable to be concatenated to full reversed message in while loop
backwords = ""

## While loop that keeps running until position is equal to first
##(negative position) -1 so loop doesn't end prematurely 
while position != (first_letter -1):
    ## Concatenate each letter to empty string "backwords"
    backwords += (message[position])
    ## Add -1 to position counter
    position -= 1

## Print final result
print ("Your message backwards is ", backwords)

input ("Press enter key to exit or should I say tixe ot yek retnE sserP")
