# Functions is a group of statements performing a specific task

# Two Types of Functions:
#     Built in Functions (len, print, range)
#     User Defined Functions


#instead of doing below code
# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
# average = (a+b+c)/3
# print(average)
# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
# average = (a+b+c)/3
# print(average)

# You can use functions:
# Function definition
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    average = (a+b+c)/3
    print(average)

# Function Call
avg() # Run the function 5 times without repeating long code
avg()
avg()
avg()
avg()

