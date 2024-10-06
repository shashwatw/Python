# Python Loops Tutorial 🔄

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](README.md)

A comprehensive guide to understanding loops in Python, from basics to practical examples.

## 📚 Table of Contents

- [Basic Loop Examples](#basic-loop-examples)
  - [Simple Loops](#simple-loops)
  - [While Loops](#while-loops)
  - [List Iteration](#list-iteration)
  - [For Loops](#for-loops)
  - [For Loop with Else](#for-loop-with-else)
  - [Pass Statement](#pass-statement)
  - [Break and Continue](#break-and-continue)
- [Practice Problems](#practice-problems)

## Basic Loop Examples

### Simple Loops

```python
# Traditional approach
print(1)
print(2)
print(3)
print(4)
print(5)

# Using loops
for i in range(1, 6):
    print(i)
```

### While Loops

```python
i = 1
while(i < 51):
    print(i)
    i += 1
```

### List Iteration

```python
l = [1, "Shashwat", False, "This", "Risha", "Sushant", "Komal"]
i = 0
while(i < len(l)):
    print(l[i])
    i += 1
```

### For Loops

```python
# Basic range loop
for i in range(4):  # 0 to 3
    print(i)

# Range with step size
for i in range(0, 100, 5):  # 0, 5, 10, ..., 100
    print(i)

# Iterating through different collections
l = [1, 4, 6, 234, 6, 724]
for i in l:  # List
    print(i)

t = (6, 231, 75, 122)
for i in t:  # Tuple
    print(i)

s = "Shashwat"
for i in s:  # String
    print(i)
```

### For Loop with Else

```python
l = [1, 7, 8]
for item in l:
    print(item)
else:
    print("done")  # Executed when loop completes normally
```

### Pass Statement

```python
# Using pass as a placeholder
for i in range(645):
    pass  # Do nothing

i = 0
while(i < 45):
    print(i)
    i += 1
```

### Break and Continue

```python
# Break example
for i in range(100):
    if(i == 34):
        break  # Exit loop
    print(i)

# Continue example
for i in range(100):
    if(i == 34):
        continue  # Skip iteration
    print(i)
```

## Practice Problems

### 1. Multiplication Table Generator

```python
num = int(input("Enter the number for table : "))
for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")
```

### 2. Name Greeting Program

```python
l = ["Shashwat", "Asmi", "Sushant", "Komal"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
```

### 3. Multiplication Table Using While Loop

```python
i = 1
num = int(input("Enter the number for its table : "))
while(i != 11):
    print(f"{num} X {i} = {num*i}")
    i += 1
```

### 4. Prime Number Checker

```python
num = int(input("Enter number : "))
isPrime = False

for i in range(2, num):
    if(num % i == 0):
        print(f"{num} is not a prime number")
        isPrime = True
        break
else:
    print(f"{num} is a prime number")
```

### 5. Sum of Natural Numbers

```python
num = int(input("Enter Number: "))
sum = 0
for i in range(1, num+1):
    sum += i
print(f"Sum of first {num} natural numbers is {sum}")
```

### 6. Factorial Calculator

```python
num = int(input("Enter the number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print(f"{num}! = {fact}")
```

### 7. Pyramid Pattern

```python
n = int(input("Enter n: "))
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("")
```

### 8. Triangle Pattern

```python
n = int(input("Enter n: "))
for i in range(1, n+1):
    print("*" * i, end="")
    print("")
```

### 9. Hollow Square Pattern

```python
n = int(input("Enter n: "))
for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")
```

### 10. Reverse Multiplication Table

```python
n = int(input("Enter n: "))
for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")
```
