# Can you change the values inside a list which is contained in set S?

S = {8, 7, 12, "Shashwat", [1,2]}

#S[4][0] = 3 # not possible as first thing is list can not be included in set and indexing is not present in set

# No, you cannot have a list inside a set in Python because lists are mutable, and all elements in a set must be immutable (i.e., hashable) and list is mutable. Instead you can have tuple in set as they are immutable and hashable. Since lists can be changed after creation, they cannot be used as elements in a set.