Student_Scores= [67,62,33,88,75,51,99,22,33,66]
for n in range(0,len(Student_Scores)):
    Student_Scores[n] = int(Student_Scores[n])
Hscore = 0
for score in Student_Scores:
    if score>Hscore:
        Hscore=score
print(f"The highest score in the clas is: {Hscore}")