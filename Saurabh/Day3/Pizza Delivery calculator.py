#Pizza Delivery Price Calculator
print("Thank you for choosing Python Pizza Deliveries!")

size = input()  # What size pizza do you want? S, M, or L
add_pepperoni = input()  # Do you want pepperoni? Y or N
extra_cheese = input()  # Do you want extra cheese? Y or N

bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    bill

if add_pepperoni == "Y" and size == "S":
    bill = bill + 2
elif add_pepperoni == "Y" and (size == "M" or size == "L"):
    bill = bill + 3
else:
    bill

if extra_cheese == "Y":
    bill = bill + 1
else:
    bill

print(f"Your final bill is: ${bill}.")