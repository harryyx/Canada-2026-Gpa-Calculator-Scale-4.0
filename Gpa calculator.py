percentage = float(input("Enter your percentage grade: "))
if percentage >= 90 and percentage <= 100:
    gpa = 4.0
    grade = 'A+'
elif percentage >= 85:
    gpa = 4.0
    grade = 'A'   
elif percentage >= 80:
    gpa = 3.7
    grade = 'A-'
elif percentage >= 76:
    gpa = 3.3
    grade = 'B+'
elif percentage >= 73:
    gpa = 3.0
    grade = 'B'
elif percentage >= 70:
    gpa = 2.7
    grade = 'B-'
elif percentage >= 67:
    gpa = 2.3
    grade = 'C+'
elif percentage >= 64:
    gpa = 2.0
    grade = 'C'
elif percentage >= 60:
    gpa = 1.7
    grade = 'C-'
elif percentage >= 55:
    gpa = 1.3
    grade = 'D+'
elif percentage >= 50:
    gpa = 1.0
    grade = 'D'
elif percentage >= 0:
    gpa = 0.0
    grade = 'F'
else:
    gpa = "Invalid percentage"

print("Your GPA is: ", gpa,"and your grade is: ", grade)
