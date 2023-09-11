# Write a Python function to calculate the factorial of a number (a non- negative integer).
# The function accepts the number as an argument

def fact(n):
    return 1 if (n==1 or n==0) else n * fact(n - 1)

num = int(input("Enter a number:"))
print(f"Factorial = ", fact(num))