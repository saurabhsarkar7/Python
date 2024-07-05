states_of_america = ["A","B","C","D","E","F"]
print (states_of_america[0])# offset 0 is the beginning
print (states_of_america[-1])# offset -1 is the ending

#how to update the values in List

states_of_america[1] = "b"
print(states_of_america)
states_of_america[1:3] = ["B","BB","BBB"] # update values multiple, first argument{index), second argument(len of list)
print(states_of_america)


#how to add/append in the list
states_of_america.append("G")
print(states_of_america)



#bunch of items to append
states_of_america.extend(["H","I","G"])
print(states_of_america)

#many more functions associate with List -->refer "docs.python.org"
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('grapes'))
print(fruits.index('banana'))
print(fruits.index('banana', 4)) # Find next banana starting at position 4
fruits.reverse() #reverse teh content in List
print(fruits)
fruits.insert(1,"grapes")
print(fruits)
fruits.sort() #sorts items in list in order
print(fruits)
print(fruits.pop(3)) # prints the last item of the List if nothing is provided else print based on index


#To calculate no.of items in the List.
A= len(states_of_america)
print(A)

#Sub Listing
List1 = ["A","B","C","D","E","F"]
List2 = ["Z","Y","X","V","U"]

List = [List1,List2]
print(List)
print(List[0])
print (List[1])
print (List[1][1])



list1 = [1,2,3,4,5]
list1.reverse()
print(list1)

#Copying list
import copy
list = [1,2]
list1 =copy.copy(list)
print(list1)

#index slicing
num = [1,3,5,7,9]
print(num[0:5]) #0 --> starting point, @end point --> length
print(num[0:]) #complete
print(num[:]) #complete
print(num[1:3])
print(num[0:5:1])# third argument is step to skip before print
print(num[0:5:2])# skip argument is 2

#insert-- one item at a time
num.insert(2,45)
print(num)
#append --one at a time
num.append(55)
print(num)
#extend -multiple data at end
num.extend([67,68,69,70])
print(num)
num1 =[1,2,3,3,3,4]
print(num.clear()) #clears everything.


#Sub -list

List1 =[7,88,91,[34,45,-1],90,12]
print(List1[3][2])