# Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter the number for table : "))

for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")