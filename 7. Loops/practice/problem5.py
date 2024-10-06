# Write a program to find the sum of first n natural numbers using while loop.

num = int(input("Enter Number: "))
sum = 0

for i in range(1, num+1):
    sum += i

print(f"Sum of first {num} natural numbers is {sum}")