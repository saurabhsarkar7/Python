states_of_america = ["A","B","C","D","E","F"]
print (states_of_america[0])# offset 0 is the beginning
print (states_of_america[-1])# offset -1 is the ending

#how to update the values in List

states_of_america[1] = "b"
print(states_of_america)
states_of_america[1] = "B"
print(states_of_america)

#how to add/append in the list
states_of_america.append("G")
print(states_of_america)



#bunch of items to append
states_of_america.extend(["H","I","G"])
print(states_of_america)

#many more functions associate with List -->refer "docs.python.org"

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