# List inbuilt methods

friends = ["Apple", "Oranges", 5, 345.06, False, "Shashwat"]
friends.append("Cherry") # adds element at the end of the list
print(friends)

l1 = [10, 4, 7, 3, 2, 9, 1, 8]

l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(2, 3333) # insert 3333 at 2 index in list
print(l1)

l1.pop(3) # pops particular(here 3) index value
# print(l1.pop(3)) # prints the popped value at particular index posn

l1.remove(10) # removes particular value from the list i.e here it removes 10 from list l1