#library import named as random
import random
#random number between two numbers
random_integer = random.randint(1,10)
print(random_integer)

#Generate random floating point number
random_float =random.random() #will give float between 0 amd 1 (Not whole number 1)
print (random_float)
# want to extend between 0 and 5

random_float =random.random() * 5
print (random_float)

#random choic with string!
password = ""
numbers= ['0','1','2','3','4','5','6','7','8','9']
nr_numbers = int(input("How many numbers would you like in your password?\n"))
for char in range(1,nr_numbers+1):
    password += random.choice(numbers)

print(password)