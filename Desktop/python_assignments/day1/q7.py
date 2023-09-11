# Write a Python program to find given number is positive ,negative or zero.

str_num = input("Enter a number:")
num = int(str_num)

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")