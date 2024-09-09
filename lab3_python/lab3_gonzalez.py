"""
Delvin Gonzalez 
lab 3, Python review
"""
print("-----------Example 1: control flow -----------")
labs = int(input("Enter labs' Grade:  "))
exams = int(input("Enter exames'grade: "))
finalgrade = 0
gpa = ''

if (0<=labs<=100 and 0<=exams<=100):
    finalgrade = (labs+exams) /2
    if (100>=finalgrade >= 90):
        gpa = 'A'
    elif (90>finalgrade>=80):
        gpa = 'B'
    elif (80>finalgrade>=70):
        gpa = 'C'
    elif (70>finalgrade>=60):
        gpa = 'D'
    elif (60>finalgrade>=0):
        gpa = 'F'
    else:
        gpa = 'UNDEFINED'
else:
    if not(0<=labs<=100):
        print(f"grade for lab {labs} is invalid")
    elif not (0<=exams<=100):
        print(f"grade for exams {exams} is invalid")
    else:
        print(f"grade for labs = {labs} and exams = {exams} are invalid")
    gpa = 'UNDEFINED'

print(f"Your final grade in the class is {finalgrade} = {gpa} ")