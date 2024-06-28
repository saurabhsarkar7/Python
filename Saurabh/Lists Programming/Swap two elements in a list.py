def swapPositions(list,pos1,pos2):

    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list

list = [23,65,19,90]
#pos1,pos2 = 0,2
pos1,pos2 = 1,3

#output: [19,65,23,90]

#print(swapPositions(list,pos1,pos2))
print(swapPositions(list,pos1 - 1,pos2 - 1))

#Way2
def swapPositions(list,pos1,pos2):
    get = list[pos1],list[pos2]
    list[pos2],list[pos1] = get

    return list

list = [23,65,19,90]
pos1,pos2 = 0,2

print(swapPositions(list,pos1,pos2))

#way3
def swapPositions(list,pos1,pos2):
    temp =list[pos1]
    list[pos1] = list[pos2]
    list[pos2] = temp

    return list

list = [23,65,19,90]
pos1,pos2 = 0,2

print(swapPositions(list,pos1,pos2))

#there could be other ways as well

