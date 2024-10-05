#  Write a program which finds out whether a given name is present in a list or not.

l = ['Shashwat', "Risha", "Sushant", "DJ"]

name = input("Enter your name : ")

if(name in l):
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")