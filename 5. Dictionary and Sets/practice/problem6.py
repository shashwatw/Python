# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

dictionary = {}

name1 = input("Enter your name : ")
lang1 = input("Enter your fav language : ")
dictionary.update({name1 : lang1})

name2 = input("Enter your name : ")
lang2 = input("Enter your fav language : ")
dictionary.update({name2 : lang2})

name3 = input("Enter your name : ")
lang3 = input("Enter your fav language : ")
dictionary.update({name3 : lang3})

name4 = input("Enter your name : ")
lang4 = input("Enter your fav language : ")
dictionary.update({name4 : lang4})

print(type(dictionary))


# Important points
# -> If keys are multiple as input then value gets updated for corresponding key
# -> If values are multiple but their keys are different then the key value pairs will be created