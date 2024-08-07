#The default values are evaluated at the point of function definition in the defining scope

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

#Important warning: The default value is evaluated only once. This makes a difference when
# the default is a mutable object such as a list, dictionary, or instances of most classes.
#For example, the following function accumulates the arguments passed to it on subsequent calls:

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

#If you don’t want the default to be shared between subsequent calls,
# you can write the function like this instead:
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

V1 =f(100)
V2 =f(20)
V3= [1000]
print(V1)
print(V2)
print(V3)

