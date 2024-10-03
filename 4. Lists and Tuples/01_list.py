
#* Python lists are containers to store a set of values of any data type
#* A list can be indexed just like strings

friends = ["Apple", "Oranges", 5, 345.06, False, "Shashwat"]
print(friends[0])

str = "Shashwat"
# str[0] = 'A' # here will give error as we can't mutate string

# But lists are mutable
friends[1] = "Cherry"
print(friends[1])
print(friends[1:4]) # slicing of lists are same as string slicing