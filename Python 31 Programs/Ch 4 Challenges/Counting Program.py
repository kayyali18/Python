## Ch 4 Challenges
## Counting program

print ("Welcome to the counter program. You give me a number to start from,\n\
a number to end at, and an interval to count by. I will then, count for you.")

minimum = int(input("What is the starting number?:\t"))
maximum = int(input("What is your ending number?:\t"))
interval = int(input("How much you want to me to skip by?:\t"))

for i in range(minimum, (maximum + 1), interval):
    print (i)

reply = input("Did I do as promised? Yes or no?:\t")

if reply.lower() == "no":
    print("Please talk to A7mad Basha and ask him to fix this code")
else:
    input("Press Enter to exit")
