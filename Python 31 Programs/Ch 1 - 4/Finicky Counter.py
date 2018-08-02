## Finicky Counter
## Demonstrate the break and continue statements

##Set variable outside of loop
count = 0
while True:
    count += 1
    # end loop if count greater than 10
    if count > 10:
        break
    # skip 5
    if count == 5:
        continue
    print(count)

input("Press Enter key to exit")
    
