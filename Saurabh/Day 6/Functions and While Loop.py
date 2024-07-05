#Functions
#built In Functions like Len, int,print etc. the name of a function is followed by ().
#Whatever inside () will be outputed in console

#use buit function starts with def <function_name>():

def my_function():
    print("Hello")
    print("Bye")

my_function()# call the function by the function name and ()

#While Loop --> Do something repeatedly until condition is true.

i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

