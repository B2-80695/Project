# Write a program that accepts a list from user and print the alternate element of list.

# def alt():
#     str = input("Enter a string:")
#     for s in str:
#         alternate = range(0, str-1, 2)
#         print(alternate)
# alt()

mylist = []
size = int(input("Enter no. of elements: "))

print('Enter',str(size),'elements:')

for i in range(size):
    data = int(input())
    mylist.append(data)

print('Alternate elements are:')

for i in range(0,size,2):
    print(mylist[i])

