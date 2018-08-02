## Vowel Remover
## Demonstrates creating new strings with a for loop

message = input ("Enter a message:\t")
new_message = ""
VOWELS = "aeiou"

print ()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print ("A new string has been created:\t", new_message)

print ("\nYour message without vowels is:\t", new_message)

input ("Press Enter key to exit")
