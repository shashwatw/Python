#  Write a fun to print sum of first n natural numbers using recursion

def sum(n):
    if(n == 1):
        return 1
    else:
        return sum(n-1) + n

n = int(input("enter n: "))

print(f"{sum(n)}")