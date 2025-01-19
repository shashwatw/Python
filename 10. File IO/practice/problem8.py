# Program to make a copy of file this.txt

with open("problem8.txt","r") as f:
    content = f.read()

with open("problem8_copy.txt", "w") as f:
    f.write(content)