name = "shashwat wankhedekar"

print(len(name)) # prints length of string
print(name.endswith("wat")) # returns bool value by checking ending value
print(name.startswith("sha")) # returns bool value by checking starting value
print(name.capitalize()) # only capitalizes first character of first word in string
print(name.title()) # capitalizes first char of each word in string
print(name.find("wankhedekar")) # finds and returns the index of first occurence of the string
replaced_name = name.replace("wankhedekar", "sir")
print(replaced_name)