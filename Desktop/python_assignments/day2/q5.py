# write a function to return simple interest

def simple(p, n, r):
    si = (p * n * r) / 100
    return si

p = float(input("Enter Principal Amount:"))
n = float(input("Enter Number Of Years:"))
r = float(input("Enter Rate Of Interest:"))

print()

print(f"Simple Interest = ", simple(p, n, r))

