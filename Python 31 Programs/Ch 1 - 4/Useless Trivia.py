
#Useless Trivia Program
## Takes info (input) from the user and gives back true but useless info
name = input("Hello, thank you for trying this useless trivia, please \n\
enter your name:  ")
print ("Okay ", name, " What I will do now is ask you a few questions and give you \n\
useless information about yourself that you probably never knew!!")
age = int(input("Okay, please tell me your age: "))
weight = int(input("One last question. Can you \n\
please enter your weight: "))

## Calls name and repeats it 5 times
called = name*5
print ("\nIf your little cousin was trying to call you")
print ("he would say: ")
print (called)

input("Press Enter")


print ("\n\n\t If I was mad at you because you broke my laptop")
print ("\n I would yell:  ", name.upper())
input("Press Enter")



### Takes input (age) and changes it from years to seconds and prints 
seconds = age * 365 * 24 *60 * 60

print ("\n You're over " , seconds, "seconds old!!!")
input("Press Enter")

## Takes input(weight) and calculates it on the moon and sun and prints

moon_Weight= weight/6

print("\n\n Did you know on the moon you would weight only  " , moon_Weight, \
      "pounds???!")
input("Press Enter")
sun_Weight = weight *27.1

print("\n\nAnd on the sun you'd weigh ", sun_Weight, "pounds (but....ahhhh....\
not for long) \n\ in the words of Mims 'This is why I'm hot'")
input("Press Enter")

print("\a")
print("Thank you ", name)
input (" Press Enter key to exit")

print("\a")
input("HAHAHA JK JK JK   \n\n\n Try it now :P")


