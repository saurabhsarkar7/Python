print("Welcome to the tip calculator!")
Bill = float(input("What was the total bill? Rs."))
Tip = int(input("How much tip would you like to give?"))
Split = int(input("How many people to split the bill?"))
tip_as_percent = Tip / 100
Actual_Tip = Bill * tip_as_percent
Final_bill = Bill + Actual_Tip
Bill_Per_Person = Final_bill/Split
Share = round(Bill_Per_Person,2)
#To restrict float to two decimal places in case of 0 at end.
Share = "{:.2f}".format(Bill_Per_Person)
print(f"Each person should pay: {Share}")