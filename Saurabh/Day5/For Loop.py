fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
    print(fruits)
print(fruits) #outside loop, see indentation


for x in "banana":
  print(x)

#break statement --> With the break statement we can stop the loop before it has looped through all the items
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Break --> case 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#With the continue statement we can stop the current iteration of the loop,
# and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Range
  for x in range(6):
      print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Break the loop when y is 3, and see what happens with the else block:

for x in range(6):
  if x == 3:
      break
  print(x)
else:
  print("Finally finished!") #Else part is not printed