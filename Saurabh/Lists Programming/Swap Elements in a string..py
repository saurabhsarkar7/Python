#Swapping elements in a string list
#Input text
test_list = ['Gfg','is','best','for','Geeks']
#Print Input Text
print("the original string is: " + str(test_list))
res = [sub.replace('G','g').replace('e','G') for sub in test_list]

print("List after performing character swaps : " + str(res))
