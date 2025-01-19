word = "Donkey"
with open("problem4.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("problem4.txt", "w") as f:
    f.write(contentNew)