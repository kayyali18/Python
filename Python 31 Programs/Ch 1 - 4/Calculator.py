print (" Please pick a number from 1-4")

operation = int(input("Please enter your number:\t"))

while operation > 4 or operation < 0:
    operation = int(input("Please enter your number:\t"))

print ("You're number is ", operation)

num_1 = int(input("Please enter your first number:\t"))
num_2 = int(input("Please enter the second number:\t"))


if operation == 1:
    print (num_1 + num_2)
elif operation == 2:
    print (num_1 - num_2)
elif operation == 3:
    print (num_1 * num_2)
elif operation == 4:
    print (num_1 / num_2)
