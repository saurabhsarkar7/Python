# Python program to interchange first nd last element in a list
#Input : [12,35,9,56,24]
#Output: [24,35,9,56,12]

#list = [12,35,9,56,24]
#print(List)
#list.reverse()
#print(List)

#Way 1
def swapList(newList):
    size =len(newList)

    temp =newList[0]
    newList[0] = newList[size -1]
    newList[size -1] = temp

    return newList

#newList = [12,35,9,56,24]
List = [12,35,9,56,24]  #after return, you can pass any variable name but ensure the same variable is passed in print.
print(swapList(List))

#way 2

def swapList(newlist):
    newlist[0], newlist[-1] = newlist[-1], newlist[0]
    return newlist

newlist = [12,35,9,56,24]
print(swapList(newlist))

#way3
def swapList(newlist):
    get = newlist[-1],newlist[0]
    newlist[0],newlist[1] = get

    return newlist

newlist = [12, 35, 9, 56, 24]
print(swapList(newlist))

#way 4 - using * --assigns a list of item
def swapList(newlist):
    start,*middle,end =  newlist
    newlist = [end,*middle,start]

    return newlist

newlist = [12, 35, 9, 56, 24]
print(swapList(newlist))

#way 5 -using pop and append
def swapList(newlist):
    first = newlist.pop(0)
    last = newlist.pop(-1)

    newlist.insert(0,last)
    newlist.append(first)

    return newlist

newlist = [12, 35, 9, 56, 24]
print(swapList(newlist))





