# Write a program that will calculate the price for a quantity entered from the
# keyboard, given that the unit
# price is Rs 5 and there is a discount of 10 percent for quantities over 30 and a 15
# percent discount for quantities over 50.

quantity = int(input("Enter the quantity:"))
unit = 5
price = quantity * unit

if quantity < 30:
    price = unit * quantity
elif quantity > 30 and quantity < 50:
    dis = (quantity * unit) * 10 / 100
    price = price - dis
else:
    dis = (quantity * unit) * 15 / 100
    price = price - dis

print(f"Total Price = {price}")