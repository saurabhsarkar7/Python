print("Welcome to Treasure Island. Your mission is to find the treasure.")
Direction = input("Which direction will you choose Left or Right? ").lower()

if Direction == "Left":
    Action = input("Which action will you perform?Swim Or Wait ").lower()
    if Action =="Wait":
        Door = input("Which door will you choose? Red or Blue or Yellow").lower()
        if Door == "Yellow":
            print("You own the game! Selected the Yellow Door")
        else:
            print("You lost the game! You did not select Yellow")
    else:
        print("You lost the game! You choose to Swim")
else:
    print("You lost the game! You choose the Right Direction")

#For multip bloc/line strings your print should strt with ''' and end with ''')


