# Write a program to print multiplication table of a given number using while loop.

i = 1

num = int(input("Enter the number for its table : "))

while(i != 11):
    print(f"{num} X {i} = {num*i}")
    i += 1