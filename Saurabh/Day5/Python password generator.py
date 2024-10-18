import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers= ['0','1','2','3','4','5','6','7','8','9']
symbols =['!','@','#','$','%','^','&','*','(',')','_','-','+','=']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols= int(input("How many symbols would you like in your password?\n"))

#Easy Level --> wDrT#$123
#hard Level --> w#2Dr23$T

#Easy Level
password = ""
#nr_letters = 4 -- assumption
for char in range(1,nr_letters+1):
    password += random.choice(letters)
    #random_char = random.choice(letters)
    #password+= random_char

for char in range(1,nr_symbols+1):
    password += random.choice(symbols)

for char in range(1,nr_numbers+1):
    password += random.choice(numbers)
#print(password) -->Easy waay
#Hard way
new_pass= ""
length= len(password)
for x in range(1, length +1):
    new_pass += random.choice(password)

print(new_pass)

#hard Way --> You can also take a list in starting instead aof avariable passorld = "" take
#password = [] , the n use random.shuffle(password0 to change the order and then run the
#for loop to randomly print the converted list into string something like this:

