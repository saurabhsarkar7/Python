#SYNTAX
# if condition:
#     <Do this>
# else:
#     <Do this>
#program to allow customer to buy tickets for roller coaster based on height

print("Welcome to the RollerCoaster Ride!")
height =int(input("what is your height in cm?"))
if height>120:
    print("you can ride the RollerCoaster")
else:
    print("You can't ride the RollerCoaster")
#Different types of operator: >,>=,<,<=,!=,==(Double Equal to compare if the left and right value same).

#odd or Evn Number
Num= int(input())
if Num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")