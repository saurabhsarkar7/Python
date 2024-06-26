#check How many times the word TRUE and LOVE appears in both of your name and then score and rate.
male_name = input("Please enter male partner name (Akash)")
female_name =input("Please enter female partner name (Saurabh)")
couple_name = male_name + female_name
lower_case =couple_name.lower()
t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
first_digit = t+r+u+e
l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
second_digit = l+o+v+e

Digit = str(first_digit) + str(second_digit)
score = int(Digit)

if score < 10 or score >90:
    print(f"Your score is {score},you go together like coke and ment")
elif score >=40 and score <=50:
    print(f"Your score is {score},you are alright together")
else:
    print(f"Your score is {score},find a new partner or jerk off in silence")

