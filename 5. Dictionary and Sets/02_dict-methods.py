# We will explore dictionary methods

marks  = {
    "Shashwat" : 100,
    "Sahil" : 56,
    "Ramesh" : 23,
    list : [100, 89, 76, 88],
    0 : "Shashwat"
}

print(marks.items()) # Returns list of key-values tuples
print(marks.keys()) # Returns all the keys present on LHS of dictionary
print(marks.values()) # Returns all the value present on RHS of dictionary
print(marks.update({"Shashwat": 99, "Renuka" : 97})) # prints andUpdates the dictionary as dic is mutable and if a key value to be updated not present, then will be added to dictionary and updated
print(marks.get("Shashwat")) # Returns value of specified keys (and value is returned eg Shashwat's marks i.e 99 is returned here)

print(marks.get("Shivika")) # as not present in dict "None  " is returned here

# NOTE : IF the key is present in dictionary then both the below syntax gives same result but incase of key not present in dict, marks.get() will give you "None" whereas marks[] will give error
print(marks.get("Shashwat"))
print(marks["Shashwat"])

# newMarks = marks.copy() # create a shallow copy of existing dictionary
# marks.clear() # clears dictionary
res = marks.pop("Shivika", "Shivika Not found") # Removes the specified key and returns its value. If the key is not found, it returns the default value (or raises a KeyError if no default is provided).
print(res)

d = {'a': 1, 'b': 2}
d.popitem()  # Output: ('b', 2), Follows LIFO principle