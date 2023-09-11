# Write a Python Program to Convert Celsius To Fahrenheit vice versa
# fahrenheit = (celsius * 1.8) + 32

str_cel = input("Enter temperature in celcius:")
cel = float(str_cel)
print(f"Temperature in fahrenheit = {(cel * 1.8) + 32}")

print()

str_far = input("Enter temperature in fahrenheit:")
far = float(str_far)
print(f"Temperature in celsius = {(far - 32) / 1.8}")



