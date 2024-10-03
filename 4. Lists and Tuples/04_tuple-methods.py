a = (1, 2, 5, 6, 1, 5, False, "Shashwat")
print(a)

no = a.count(5) # Counts the number of type value appeared in the tuple
print(no)

indexOfNum = a.index(2) # Returns the index of first occurence of the given input element
print(indexOfNum)

repeatedTuple = (1, 2, 3)
print(repeatedTuple * 3) # Repeat a tuple multiple times using the * operator.

len(a) # Get the number of elements in the tuple.
print(2 in a) # Returns boolean value is input element is present/absent. Checking Membership

print(a+repeatedTuple) # Concatenation: Combine two or more tuples using the + operator.

# Min and max values of the tuple
print(min(repeatedTuple))
print(max(repeatedTuple))

# Unpacking of tuples in the variables
p, q, r = repeatedTuple
print(p, q, r)