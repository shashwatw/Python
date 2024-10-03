# Dictionary is the collection of keys-valued pairs

marks  = {
    "Shashwat" : 100,
    "Sahil" : 56,
    "Ramesh" : 23,
    list : [100, 89, 76, 88]
}

print(marks, type(marks)) # type is class dict
print(marks["Shashwat"]) # gives marks of Shashwat
print(marks[list]) # prints list i.e [100, 89, 76, 88]

# NOTE: Here lookup of value is very fast i.e in O(1) time complexity whereas list would take greater time complexity

#* Properties of python dictionaries
# 1. It is unordered
# 2. It is mutable
# 3. It is indexable
# 4. Cannot contain duplicate keys

