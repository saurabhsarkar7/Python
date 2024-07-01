Student_Heights = ['151','145','179']
Height = 0
for n in range(0,len(Student_Heights)):
    Student_Heights[n] = int(Student_Heights[n])
    Height = Height + Student_Heights[n]
Total_Height = Height
Count = len(Student_Heights)
Average_Height = round((Total_Height/Count))

print(f"Total Height = {Total_Height}")
print(f"Number Of Students = {Count}")
print(f"Average Height = {Average_Height}")

