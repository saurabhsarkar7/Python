#syntaxnested if

# if condition:
#     if another condition:
#         do this:
#     else:
#         do this


print("Welcome to the RollerCoaster Ride!")
height =int(input("what is your height in cm?"))
if height>120:
    print("you can ride the RollerCoaster")
    age =int(input("What is your age?"))
    if age < 12:
        print("Pay Rs.100")
   # elif age >= 12 and age < 18:
    elif age <=18:
        print ("Pay Rs.200")
    #elif age>=18:
    else:
        print("Pay Rs.500")
else:
    print("You can't ride the RollerCoaster")
#Different types of operator: >,>=,<,<=,!=,==(Double Equal to compare if the left and right value same).
