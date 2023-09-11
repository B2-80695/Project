# write a function to return compound interest

def compound(p, n, r):
    amt = p * (pow((1 + r / 100), n))
    ci = amt - p
    return ci

p = float(input("Enter Principal Amount:"))
n = float(input("Enter Number Of Years:"))
r = float(input("Enter Rate Of Interest:"))

print()

print(f"Compound Interest = ", compound(p, n, r))