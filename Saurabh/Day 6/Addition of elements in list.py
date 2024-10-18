my_list =[11,12]
i=0

while len(my_list) < 4:
    my_list.append(i)
    i+=5

print(my_list)

#Number Series

n = 10

while n <= 100:
    print(n) #print(n,end = ",") in one row
    n = n+10

#Sum of a number in list

myList = [23,45,12,10,25]
i =0
sum =0

while i < len(myList):
    sum = sum + myList[i]
    i= i+1

print(sum)

#Printing all letters except some using Python while loop
i = 0
word = "Hello"

#print all letters except e and o


while i < len(word):
    if word[i] == "e" or word[i] =="o":
        i += 1
        continue

    print("Returned letter",word[i])
    i += 1