# Python program to interchange first nd last element in a list
#Input : [12,35,9,56,24]
#Output: [24,35,9,56,12]

#list = [12,35,9,56,24]
#print(List)
#list.reverse()
#print(List)
def swapList(newList):
    size =len(newList)

    temp =newList[0]
    newList[0] = newList[size -1]
    newList[size -1] = temp

    return newList

#newList = [12,35,9,56,24]
List = [12,35,9,56,24]  #after return, you can pass any variable name but ensure the same variable is passed in print.
print(swapList(List))



