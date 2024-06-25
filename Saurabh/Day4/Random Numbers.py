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

