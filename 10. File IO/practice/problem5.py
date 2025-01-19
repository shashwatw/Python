words = ["Donkey", "cheating", "failure"]
with open("problem5.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("problem5.txt", "w") as f:
    f.write(content)