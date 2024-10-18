#The first program
print("Hello World!")
#Different ways to accomodate special characters in a print statement
print("1. Add '3gm.' of salt")
print('1. Add "3gm." of salt')
print("1. Add \"3gm.\" of salt")
#print raw strings - below example shows \n is not printing in new line as wea re using "r" option.
print(r"C:\doc\navin")
#Print in new lines using \n operator
print("Helo World!\nHello World!\nBye World!")
#Concatenation
print("Hello" + " " +"Saurabh"+ "!")
#Input Function
input("what is your name?")
#Print with Input Function
print("Hello " + input("What is your name?"))
print(input())
#Print with  variables
num1 =int(input ())
num2 = int(input())
print(num1 * num2)
#print len output
A = len("Saurabh")
print(A)
#OR
print(len(input()))
#memomory of the dat storage/ ID
a= 5
b =5
print(id(a))
print (id(b))
#different memory allocated
a =6
b=5
print(id(a))
print (id(b))