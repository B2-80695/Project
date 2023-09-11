# Write a Python Program Get age input from user and check if user is eligible for voting

str_age = input("Enter an age:")
age = int(str_age)

if age >= 18:
    print(f"Eligible for voting")
else:
    print(f"Not eligible for voting")