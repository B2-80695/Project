 # Replace single element ‘b’ in given list [’a’, ’b’, ’c’, ’d’, ’e’] with [1, 2, 3].

def str():
     # printing original list
     list = ["a", "b", "c", "d", "e"]
     print(list)

     print("After removing b:")

     # removing b
     list.remove('b')
     print(list)

     print("After inserting 1, 2, 3:")

     # inserting 1,2,3
     list.insert(1, 1)
     list.insert(2, 2)
     list.insert(3, 3)

     print(list)

str()
