## Loopy String
## Demonstrates the for loop with a string

word = input ("Enter a word:\t")
count = 0

print ("\nHere's each letter in your word:")
for letter in word:
    print (letter)
    count += 1

print ("Number of letters is:\t", count)

input ("\n\nPress Enter key to exit")

## For Loops and Counting
## Demonstrates the range() function

print ("Counting:")

## Counts the numbers in a certain range
for i in range (10):
    print (i, end=" ")

## Counts numbers in range by fives
print ("\n\nCounting by fives:")
for i in range (0, 50, 5):
    print (i, end=" ")

## Counts numbers in range backwards
print ("\n\nCounting backwards:")
for i in range (10, 0, -1):
    print (i, end=" ")

input ("Press Enter key to exit")

## Redundant loops to create multiples of something

print ("\n\nI will print 'Hello World!' 10 times")

for i in range (10):
    print ("Hello World!")

input ("Press Enter to exit")
