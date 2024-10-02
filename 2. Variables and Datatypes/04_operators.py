
#! Operators in python

#* 1. Arithmetic Operators : +, -, *, /, etc.
#* 2. Assignment Operators : =, +=, -=, etc.
#* 3. Comparison Operators : ==, >=, <=, !=, etc.
#* 4. Logical Operators    : and, or, not.

#? ****************************************************************************************************************************

#* 1. Arithmetic Operators
a = 7
b = 4
c = a + b
print(c)

#* 2. Assignment Operators
a = 4-2 # Assign 4-3 in variable a
print(a)
b = 6
# b += 3 # Increment value of b by 3 and assign it to b
b -= 3 # Decrement value of b by 3 and assign it to b
print(b)

#* 3. Comparison Operators
d = 5 < 4
e = 5 == 5
print(d)
print(e)

#* 4. Logical Operators
e = True or False # is true
f = True and False # is false
#& You know truth table already
print(e)

print(not(True)) # will give false
print(not(False)) # will give true