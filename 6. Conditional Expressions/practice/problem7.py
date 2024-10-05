# Write a program to find out whether a given post is talking about "Shashwat" or not.

post = input("Enter the post: ")

if("Shashwat".lower() in post.lower()): # then the findings will not be case sensitive and if word present then will tell its presence
    print("This post is talking about Shashwat")
else:
    print("This post is not talking about Shashwat")