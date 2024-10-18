#key word argument
# Keyword Arguments
# Functions can also be called using
# keyword arguments of the form kwarg=value. For instance, the following function:
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")



#p1 = parrot(1000)                                          # 1 positional argument
# p2 = parrot(voltage=1000)                                  # 1 keyword argument
# p3 = parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# p4 = parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
p5 = parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# p6 = parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

print(p5)

#It accepts one required argument (voltage) and three optional arguments (state, action, and type).
#This function can be called in any of the following ways:

#all the following calls would be invalid:

# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument