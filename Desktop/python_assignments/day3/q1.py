# # Using for loop, write and run a Python program to find factorial from 0 to 10

def factorial(n):
    result = 1
    for x in range(1, n+1):
        result = result * x
    return result

for n in range(1,11):
    print(n, factorial(n))