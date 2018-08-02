## Message Analyser
## Demonstrates the len() function and the "in" operator

message = input ("Enter a message:\t")

print ("\nThe length of your message is:\t", len(message))

print ("\nThe most common letter in the English language, 'e',")
if "e" or "E" in message:
    print ("is in your message")
else:
    print ("is not in your message")

input ("\n\nPress Enter key to exit")


##Indexing and random access
## Demonstrates string indexing

import random

word = "index"
print ("The word is:\t", word, "\n")

high = len (word)
low = -len (word)

for i in range(10):
    position = random.randrange(low, high)
    print ("word[", position, "]\t", word[position])

input ("Press Enter key to exit")

    
