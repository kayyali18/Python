# Write it program
# Demonstrating how to write to files.

print ("\nCreating a text file with the write() method!")

text_file = open ("read_this.txt", "w")
text_file.write ("Line 1\n")
text_file.write ("This is line 2\n")
text_file.write ("That makes this line 3\n")
# Closing text file
text_file.close ()

# Checking to see if it works
input ("\nReading the newly created file")

text_file = open ("read_this.txt", "r")
print (text_file.read())

input ("\nCreating a text file, with the writelines () method")

# Writing to a file using a list
text_file = open ("read_this.txt", "w")
# creating list
lines = ["Line 1 \n",
         "This is line 2\n",
         "That makes this line 3\n"]
text_file.writelines(lines)

# close the file, good practice
text_file.close ()

print ("\nReading the newly created file")

# opening file
text_file = open ('read_this.txt', 'r')


print (text_file.read())

input ("\nPress Enter key to exit")
