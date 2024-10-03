s1 = {1, 45, 6, 78}
s2 = {7, 8, 1, 78}
   
print(s1.union(s2)) # It is union that consists every unique element
print(s1.intersection(s2)) # It is intersection thst consists each common unique element

# Other operations

# 1. issubset(other_set): Returns True if all elements of the current set are in the other set.
s1 = {1, 2}
s2 = {1, 2, 3}
print(s1.issubset(s2))  # Output: True  

# 2. issuperset(other_set): Returns True if all elements of the other set are in the current set.

s1 = {1, 2, 3}
s2 = {1, 2}
print(s1.issuperset(s2))  # Output: True