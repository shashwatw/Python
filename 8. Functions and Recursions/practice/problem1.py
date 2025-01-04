# Write a prog using func to find greatest of 3 nums

def greaterFun(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print(f"Greatest of {a}, {b} and {c} is {greaterFun(a,b,c)}")