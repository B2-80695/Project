# Write a Python function to find the maximum of three numbers.

str_num1 = input("Enter 1st number:")
num1 = int(str_num1)

str_num2 = input("Enter 2nd number:")
num2 = int(str_num2)

str_num3 = input("Enter 3rd number:")
num3 = int(str_num3)

if num1 > num2 and num1 > num3:
    max = num1
elif num2 > num3 and num2 >num1:
    max = num2
else:
    max = num3

print(f"The maximum of three numbers = {max}")