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

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#for loops cannot be empty, but if you for some reason have a for loop with no content,
#put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass

#sum of digits between 1 and 100
total = 0
for number in range(1,101):
  total = total + number
print(total)

#Sum of even digits between 1 and 100
total_even = 0
for x in range(1,101):
  if x % 2 == 0:
    total_even = total_even + x
print(total_even)
