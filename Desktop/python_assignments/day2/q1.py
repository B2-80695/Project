# Write a program that prompts the user to input a year and determine whether the
# year is a leap year or not. Leap Years are any year that can be evenly divided by 4.
# A year that is evenly divisible by 100 is a leap year only if it is also evenly divisible by
# 400.
# Example :
# 1992 Leap Year
# 2000 Leap Year
# 1900 NOT a Leap Year
# 1995 NOT a Leap Year
# (Year % 400 == 0) or. (Year % 100 != 0) and. (Year % 4 == 0)

year = int (input("Enter an year:"))

if(year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print(f"This is a leap year")
else:
    print(f"This is not a leap year")
