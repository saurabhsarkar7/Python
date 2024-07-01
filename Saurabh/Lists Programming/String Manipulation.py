List =  ["Saurabh","Sunil","Sandeep"]
a= List[0]
b = len(a)
c = ''
for i in range(len(a),0,-1):
    c+= a[i-1]
    z =c
print(z)

#membership operator
str = ('Jerry')
print('r' not in str)

l1= [1,10,20,21,99]
print(1 not in l1)
