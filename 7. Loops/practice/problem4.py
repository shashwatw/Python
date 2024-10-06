# Write a program to find whether a given number is prime or not.

num = int(input("Enter number : "))
isPrime = False

for i in range(2, num):
    if(num % i == 0):
        print(f"{num} is not a prime number")
        isPrime = True
        break;
else:
    print(f"{num} is a prime number")