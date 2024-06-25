print("Welcome to the RollerCoaster Ride!")
height =int(input("what is your height in cm?"))
age = int(input("what is your age?"))
bill =0
if height>120:
    print("you can ride the RollerCoaster")
    if age < 12:
        bill = 25
        print("you have to pay 25")
    elif age < 18:
        bill = 35
        # print("you have to pay 35")
    else:
        bill =50
        print ("you have to pay 50")

    wants_pic = input("Do you want a photo taken? Y or N ")
    if wants_pic == "Y":
        bill = bill + 3
        print(f"Your final bill is {bill}")
    else:
        print(f"your bill is {bill}")
##
else:
    print("You can't ride the RollerCoaster")
 
