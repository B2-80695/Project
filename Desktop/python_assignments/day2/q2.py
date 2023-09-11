# The marks obtained by a student in 3 different subjects are input by the user. Your
# program should calculate the average of subjects and display the grade. The student
# gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F

s1 = int(input("Enter marks in 1st subject:"))

s2 = int(input("Enter marks in 2nd subject:"))

s3 = int(input("Enter marks in 3rd subject:"))

average = (s1 + s2 + s3) / 3
print(f"Average of subjects = {average}")

if(average >= 90 and average <= 100):
    print("Grade: A")
elif(average >= 80 and average <= 89):
    print("Grade: B")
elif(average >= 70 and average <= 79):
    print("Grade: C")
elif(average >= 60 and average <= 69):
    print("Grade: D")
else:
    print("Grade: F")


