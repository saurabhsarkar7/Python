import random

name = ["Pawan","Avijit","Chetan","Prabhat","Dipanshu","Saurabh"]
len_name = len(name)

random_choice = random.randint(0,len_name-1)
print(f"{name[random_choice]} is going to pay the bill.")

