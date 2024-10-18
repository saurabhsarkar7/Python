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
password_list = []
#nr_letters = 4 -- assumption
for char in range(1,nr_letters+1):
    password_list += (random.choice(letters))
    #random_char = random.choice(letters)
    #password+= random_char

for char in range(1,nr_symbols+1):
    password_list += random.choice(symbols)

for char in range(1,nr_numbers+1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

new_pass= ""
for x in password_list:
    new_pass += x

print(f"My new hard way to produce strong password is {new_pass}")


#print(new_pass)
