##Exclusive Network Program
## Demonstrates logical operators and compound conditions

print("\tExclusive Computer Network")
print("\tMembers Only!\n")

##Set variable (security) outside while loop
security = 0

##Set other variable (username) outside loop

username = ""
## "not" operator makes the value opposite of what it is
##Eg. var username is currently false - because of empty string \
## not username means username = "" is actually True not False


while not username:
    username = input("Username:\t")
##Set variable password outside of following while loop
password = ""
while not password:
    password = input("Password:\t")

##If else statements to complete the while loops and set the \
## database for all available users

if username == "M.Dawson" and password == "secret":
    print ("Hi, Mike.")
    security = 5
elif username == "kayyali18" and password == "abcdef6264":
    print ("Welcome, A7mad Basha+")
    security = 2
elif username == ("Aucky") and password == ("onthegrind"):
    print("Welcome Aucky, congratulations! You deserve it!")
    security = 5
elif username == ("Manasra") and password == ("mustangbaby"):
    print("Esh ya Manaseeeeerr!")
    security = 3
elif username == ("BLACK SERIES") and password == ("koks"):
    print("Allah 3lek ya BLACK WALEEDIES, welcome!")
elif username == "guest" or password == "guest":
    print("Welcome, guest.")
    security = 1
else:
    print("Login failed. You're not so exclusive.\n")

input("Press Enter key to exit")
