#BMI Calculator

weight =int(input())
height = float(input())
bmi = weight/(height)**2
print(bmi)
if bmi <18.5:
    print(f"{bmi}-underweight")
elif  bmi<25:
    print(f"{bmi}-normal weight")
elif bmi<30:
    print(f"{bmi}-slightly over weight")
elif bmi <35:
    print(f"{bmi}-obese")
else:
    print(f"{bmi}-clinically obese")