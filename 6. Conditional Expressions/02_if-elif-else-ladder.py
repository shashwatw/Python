a = int(input("Enter your age : "))

# if elif else ladder
if(a >= 18):
    print("You are above the age of consent !")
elif(a < 0):
    print("You are entering invalid age !")
else:
    print("You are below the age of 18")

print("End of program")

# Elif Statements
# 1. There can be any number of elif statements.
# 2. Last else is executed only if all the conditions inside elifs fail.