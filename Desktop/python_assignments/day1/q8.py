# Write a program that prompts the user to input number of calls and
# calculate the monthly telephone bills
# as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.

str_calls = input("Enter the number of calls:")
calls = int(str_calls)

if calls <= 100:
    bill = 200

elif calls > 100 and calls <= 150:
    bill = 200 + ((calls-100) * 0.60)

elif calls > 150 and calls <=200:
    bill = 200 + (calls-150) * 0.50 + 50*0.6

else:
    bill = 200 + ((calls-200) * 0.40) + (50*(0.6+0.5))

print(f"Monthly Bill = Rs. {bill}")
