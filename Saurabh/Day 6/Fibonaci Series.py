def fib(n):
 a,b = 0,1
 while a < n:
  print(a,end = ' ')
  a,b = b, a+b
 # print()

fib(10)

#Function that returns a list of the numbers of the Fibonacci series, instead of printing it:

def fib2(n):  # return Fibonacci series up to n
 """Return a list containing the Fibonacci series up to n."""
 result = []
 a, b = 0, 1
 while a < n:
  result.append(a)  # see below
  a, b = b, a + b
 return result

f100 = fib2(100)  # call it
#To validate and check output
print(f100)


#Default Argument Values
#The most useful form is to specify a default value for one or more arguments. This creates a
# function that can be called with fewer arguments than it is defined to allow. For example:


