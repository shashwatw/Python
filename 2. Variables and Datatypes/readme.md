# Python Fundamentals - Variables, Data Types & Operators

A comprehensive guide to Python variables, data types, operators, and basic programming concepts with examples and important rules.

## 📋 Table of Contents

- [Variables](#variables)
- [Data Types](#data-types)
- [Naming Rules](#naming-rules)
- [Operators](#operators)
- [Type Casting](#type-casting)
- [Input Operations](#input-operations)
- [Practice Problems](#practice-problems)
- [Important Rules & Notes](#important-rules--notes)

## 🔢 Variables

Variables are containers for storing data values. Here's how to declare variables in Python:

```python
a = 1
b = 2
name = "Shashwat"  # string datatype

print(a+b)  # Output: 3
```

## 📊 Data Types

Python has several built-in data types:

```python
a = 1        # Integer
b = 5.22     # Float
c = "Shashwat"  # String
d = False    # Boolean
e = None     # NoneType
```

## ⚠️ Naming Rules

Important rules for naming variables in Python:

```python
# Valid variable names
a = 23
aaa = 435
shashwat = 43
_shashwat = 89

# Invalid variable names (NOT ALLOWED)
# @shashwat = 67
# 1variable = 89
# my-var = 90
# my var = 78
```

### 🚫 Critical Rules to Remember:

1. Variable names can only contain:
   - Letters (a-z, A-Z)
   - Numbers (0-9)
   - Underscores (\_)
2. Must start with a letter or underscore
3. Cannot start with a number
4. No special characters (@, #, %, etc.)
5. Case-sensitive (`name` ≠ `Name`)
6. No Python keywords allowed

## 🔧 Operators

Python supports various types of operators:

### 1. Arithmetic Operators

```python
a = 7
b = 4
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a ** b) # Exponentiation
```

### 2. Assignment Operators

```python
a = 4
b = 6
b += 3  # Same as b = b + 3
b -= 3  # Same as b = b - 3
```

### 3. Comparison Operators

```python
print(5 < 4)   # False
print(5 == 5)  # True
print(5 != 4)  # True
```

### 4. Logical Operators

```python
print(True or False)   # True
print(True and False)  # False
print(not True)        # False
```

## 🔄 Type Casting

Convert between different data types:

```python
b = 5.67
b = int(b)    # Convert to integer
print(type(b))  # <class 'int'>

num = "123"
num = int(num)  # String to integer conversion
```

## ⌨️ Input Operations

```python
# Taking integer input
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("Sum is:", a + b)
```

## 💡 Practice Problems

1. Basic Addition

```python
a = 1
b = 2
print(a + b)
```

2. Finding Remainder

```python
a = int(input("Enter number: "))
z = int(input("Enter z: "))
print("Remainder:", a % z)
```

3. Average Calculator

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Average:", (a + b)/2)
```

## 📝 Important Rules & Notes

1. Python is dynamically typed - no need to declare variable types
2. Use `**` for exponentiation, not `^`
3. Type casting is important when working with input functions
4. All input values are strings by default
5. Variable names are case-sensitive
6. Use meaningful variable names for better code readability

## 🔍 Common Mistakes to Avoid

1. Using special characters in variable names
2. Starting variable names with numbers
3. Using Python keywords as variable names
4. Forgetting to type cast input values
5. Using spaces in variable names
