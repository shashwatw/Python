# Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter n: "))

for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")

#change from->to
# 1 --> 10
# 2 --> 9
# 3 --> 8
# 4 --> 7
# 5 --> 6
# 6 --> 5
# 7 --> 4
# 8 --> 3
# 9 --> 2
# 10--> 1