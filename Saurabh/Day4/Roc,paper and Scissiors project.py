import random
user_choice = int(input("what user is going to choose?bType 0 for Rock,1 for paper or 2 for scissiors \n"))
computer_choice = random.randint(0,2)
print (f"Computer choose {computer_choice}")

if user_choice >=3 or user_choice< 0:
    print("You typed an invalid number, you loose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice ==0  and user_choice == 2:
    print("you loose!")
elif computer_choice > user_choice:
    print("You loose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("It's a draw!")
else:
    ("You typed an invalid number, you loose!")

#using game images , dedicate some images to var Rock,paare and scissor, put them in List and substitute in
#above variables in program







