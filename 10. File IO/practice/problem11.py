# Rename a file (making a copy with renamed file)

with open("problem11.txt", "r") as f:
    content = f.read()

with open("problem11_renamed.txt", "w") as f:
    f.write(content)