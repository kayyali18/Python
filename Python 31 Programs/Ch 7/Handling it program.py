## Handle it Program
## Demonstrates how to handle errors or exceptions

## Uses the 'try' and 'except' methods

# try/except

try:
    num = float(input("Enter a number:\t"))
except:
    print ("Something went wrong!")
else:
    print ("You typed:\t", num)

# Specifying exception type
try:
    num = float(input("Enter a number:\t"))
except ValueError:
    print ("That was not a number")
else:
    print ("You entered:\t", num)

# Handling for multiple exceptions

print ()
for value in (None, "Hi!"):
    
    try:
        print ("Attempting to convert", value, "--->", end = " ")
        print (float(value))
    except (ValueError, TypeError):
        print ("Something went wrong!")

# handling multiple exceptions
# using multiple except clauses
print ()

for value in (None, "Hi!"):
    try:
        print ("Attempting to convert", value, "--->", end = " ")
        print (float(value))
    # first except clause
    except ValueError:
        print ("I can only convert a string of digits, not any string")
    # second except clause
    except TypeError:
        print ("I can only convert a string or a number!")

# showing python's official exception argument

for value in (None, "Hi!"):
    try:
        print ("Attempting to convert", value, "---->", end = " ")
        print (float(value))
    # specifying error type, and setting python's error argument to variable 'e'
    except ValueError as e:
        print (e)
    except TypeError as e:
        print (e)

input ("\n\nPress Enter key to exit")

    
        
