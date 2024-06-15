print(len("12345")) # if we dont give quotes, it will be consider as an int and throw error
#Sub-scripting
print("Hello"[0])
#Requirement for convertimg data type:
#String
print("123" + "345")
#Int
print(123+345)
#large numbers can be sepearatedby underscore instead what we use comma
print(123_789_11 + 567_435_11)
#Float
print(123.4566778)
#Boolean - True/False or (T/F)

#type Function tells about data type
num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print (num_char)
type(num_char)

#The below statement will throw an error as we ware trying to concatenate string with number
#print("Your name has " + num_char + " characters.")
#To resolve this either take num_char in a new variable and change data type
# or before len use Str function or in the final print use STR before num_char
print("Your name has " + str(num_char) + " characters.")
print("Your name has " + new_num_char + " characters.")
#mathematical operations: = +,-,*,**(To the power), Op of / is always float.
#follows Bodmas rule
#round
print(8/3) #Automatically gives float
print(int(8/3)) #gives int, removes precisions   OR
print(8//3) #same result - flow division
print(round(8/3,2)) #gives two decimals places rounded off
#Way of storing values
a= 9
a +=3
print(a)
# this means the same as a = a +3

#f-string allows you not to write always str for data conversion. Example Below:
score = 0
height = 1.8
IsWinning = True

print(f"your score is {score},your height is {height},your winning is {IsWinning}")
