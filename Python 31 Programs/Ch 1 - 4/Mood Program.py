##Mood Computer
## Demonstrates the "elif" Clause
## This program supposedly tell the user his current mood

import random
print ("I am sensing your energy. \
Your \ntrue emotions are coming across my screen.")

input("\tYou are.....")

mood = random.randint (1,3)

if mood == 1:
    #Happy mood
    print ( \
    """
-----------
|         |
| O     O |
|    <    |
|         |
| .      .|
|  ` ...` |
-----------

""")
elif mood == 2:
    #Neutral mood
    print (\
        """
-----------
|         |
| O     O |
|    <    |
|         |
| ------- |
|         |
-----------
    """)
elif mood == 3:
    #Sad mood
    print (\
        """
-----------
|         |
| 0     0 |
|    <    |
|         |
|   . ' . |
|  '     '|
-----------

    """)

else:
    print("Illegal mood value! (You must be in a really bad mood).")

print ("...today")

input ("Press the Enter key to exit ")
