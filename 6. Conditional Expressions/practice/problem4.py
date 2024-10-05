# Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter Username : ")

if(len(username) < 10):
    print("Username is of length less than 10 characters")
else:
    print("Username is greater or equal to 10 characters")