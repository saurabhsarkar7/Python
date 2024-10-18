#round(<arg1>,<arg2>) #round(value,no.of digits to be rounded off)

print(round(7.12222,2))
print(round(7.12222,0)) # As the input is float and we are putting the second argument as 0 ,O/P is float
print(round(7.12222)) #As there is no second argument, O/P is int
print(round(7,2))
print(round(674,-1))
#How to get negtaive round off
# 10 to the power negation of second argument
# 10 to the power -(-1) which is 10
# and then nearest multiple of 674 which is 670 is the output.