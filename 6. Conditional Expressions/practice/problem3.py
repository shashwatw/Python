# A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter the message : ")

# use of in keyword to check that is the phrase present in particular string...it gives boolean value and can be used in if else logic

if((p1 in message) or (p2 in message) or (p3 in message)):
    print("This message is a spam !")
else:
    print("Comment is not a spam")