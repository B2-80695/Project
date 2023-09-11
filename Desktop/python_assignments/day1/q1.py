# Write a Python Program find an area of a rectangle and perimeter of the rectangle

str_length = input("Enter the length of a rectangle:")
length = float(str_length)

str_breadth = input("Enter the breadth of a rectangle:")
breadth = float(str_breadth)

print(f"Area of a rectangle = {length * breadth}")

print(f"Perimeter of a rectangle = {2 * (length + breadth)}")