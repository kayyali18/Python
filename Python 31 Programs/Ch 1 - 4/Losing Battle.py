##Losing battle
## This program is intended to demonstrate the infinite loop
## I intend to write this program without an infinite loop

print("Your lone hero is surrounded by a massive army of trolls!")
print("Their decaying green bodies stretch out, melting into the horizon")
print("Your hero unsheathes his sword for the last fight of his life. \n")

health = 20
trolls = 0
damage = 3

while health > 0:
    trolls += 1
    health -= damage

    print("Your hero swings and defeats an evil troll, " \
          "but take", damage, "damage points. \n")

print("Your hero fought valiantly and defeated", trolls, "trolls."\
      "But alas, your hero is no more.")
input("Press Enter key to exit")
