
#* Properties of Sets :
# 1. Sets are unordered -> Element's order does not matter
# 2. Sets are unindexed -> Cannot access elements through indices
# 3. There is no way to change items in set
# 4. Sets cannot contain duplicate values

# Methods of set

isSet = {1, 5, 5, 32, 54, 5, 5, 5, "Shashwat"}
# print(isSet, type(isSet))

isSet.add(566)
print(isSet, type(isSet))

# add(element) #Adds a single element to the set.
# remove(element) #Removes the specified element from the set. Raises a KeyError if the element is not found.
# clear() #Removes all elements from the set, leaving it empty.
# pop() #Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.  
print(len(isSet)) # prints length of set
