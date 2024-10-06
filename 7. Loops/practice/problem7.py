'''
Write a program to print the following star pattern. 
   *
  ***
 ***** for n = 3
'''

n = int(input("Enter n: "))

for i in range(1, n+1):
    print(" " * (n-i), end = "") # this end ensures that new line is not made
    print("*" * (2*i-1), end = "")
    print("")