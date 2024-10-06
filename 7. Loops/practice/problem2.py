# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Shashwat", "Asmi", "Sushant", "Komal"]

name = input("Enter your name : ")

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")