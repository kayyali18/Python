####  Three programs
#### 1. Food concatenator
#### 2. Tipper Program
#### 3. Car Salesman Program


##Asks user for two favourite foods and adds them together

fav_1 = input("Please tell me your favourite food: ")
fav_2 = input("What's your next most favourite food: ")
##Concatenates input(1 + 2)
fav_together = fav_1 + fav_2

print("Your favourite food in one is " , fav_together)
#########################################################

##Tipper program that tells how much one needs to tip

bill = int(input("Please enter your bill total:  "))

tip_15 = bill*.15
tip_20 = bill*.2

print ("15% tip:   $", tip_15)
print ("20% tip:   $", tip_20)

input("Press enter to continue")

#Program to calculate total price of car after add-ons, tax, etc.

car = input("What is the model of the car?:\t")
car_base = int(input("Please enter the price of your vehicle:\t"))
tax = car_base*.0714
licensing = car_base*.0523
destination_charge = 500
dealer_charge = 275
###Sums up all the costs together for actual cost
car_actual = car_base+tax+licensing+destination_charge+dealer_charge

print("Your" ,car, "will actually cost you a total of:\t\t $", car_actual)

input("Press enter to confirm car selection")

