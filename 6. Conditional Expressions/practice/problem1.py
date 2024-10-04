# Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

if(a > b and a > c and a > d):
    print("a is largest of 4")
elif(b > a and b > c and b > d):
    print("b is largest of 4")
elif(c > b and c > a and c > d):
    print("c is largest of 4")
elif(d > b and d > c and d > a):
    print("d is largest of 4")