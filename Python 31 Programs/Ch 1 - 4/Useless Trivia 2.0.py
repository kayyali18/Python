#Useless Trivia Program
## Takes info (input) from the user and gives back true but useless info:
name = input("What's up, hello and welcome! This is a \n\
useless trivia. Enjoy!! \n\n\n\t Please enter your name:\t")
age = int(input("Okay, here's the deal.......dude! You \n\
must be at least 45 years of age to play this game.\n\
How old are you....really?\t:"))
##Trying to create if else statement to help catch people \n
##who try to cheat the age. If user is under 45 \n
## Program will terminate, by bug not by code.
if age < 45:
    print ("Pfffffftttt!! I said 45 or over, get over it!")
    sys.exit("This program refuses to accomodate the youngsters")
    


weight = int(input("One more question. \n\
How fat are you.....in pounds\t:"))

##Calls name and changes it to a nickname
called = name + " Basha+"
print ("If I was to give you a nickname, I would call you\n", \
       "\t", called)
input ("Press Enter for the next useless bit of info")

print (" If I was going to yell your nickname.", \
       "I would say ", called.upper())

input ("Press Enter to keep keepin' on")
##Takes input of (Age) and changes it from years \n
##to seconds and prints result
seconds = age * 365 * 24 * 60 * 60

print ("Okay so I did a little math, and I came up\n\
with your age in seconds: ", "\nYou're actually " , seconds, \
"old!")

##Takes input (Weight) and calculates weight on moon

moon_Weight = weight/6

print ("\n Okay so on the moon, you'll obviously be \
a lot lighter. \n ", called, " On the moon you weigh", \
moon_Weight, "lb")

input("To find out your weight on the sun, press Enter")

sun_Weight = weight*27.1

print (called, " If you manage to live long enough on the sun. \n", \
       "You would weigh, " , sun_Weight, "lb")

print ("\n\n Thank you for playing this game with me", \
       "\n I hope you enjoy the rest of your day!")
input("\n\n\t Press Enter to exit")
