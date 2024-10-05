# 🐍 Python Conditional Statements Master Guide

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Documentation](https://img.shields.io/badge/documentation-yes-brightgreen.svg)
![Maintained](https://img.shields.io/badge/maintained-yes-green.svg)

> A comprehensive guide to mastering Python conditional statements with practical examples and real-world applications.

## 📑 Table of Contents

- [Core Concepts](#-core-concepts)
- [Basic Examples](#-basic-examples)
- [Practice Problems](#-practice-problems)
- [Advanced Topics](#-advanced-topics)
- [Installation & Usage](#-installation--usage)
- [Contributing](#-contributing)

## 🎯 Core Concepts

### What are Conditional Statements?

Conditional statements are decision-making components that direct program flow based on specific conditions.

### Types of Operators

#### 1. Relational Operators

```python
==    # Equal to
>=    # Greater than or equal to
<=    # Less than or equal to
>     # Greater than
<     # Less than
!=    # Not equal to
```

#### 2. Logical Operators

```python
and    # Both conditions must be true
or     # At least one condition must be true
not    # Inverts the condition
```

## 💻 Basic Examples

### 1. Simple If-Else Statement

```python
# Basic age verification
a = int(input("Enter your age : "))

# The spacing is called indentation
if(a >= 18):
    print("You are above the age of consent !")
else:
    print("You are below the age of 18")
```

### 2. If-Elif-Else Ladder

```python
# Multiple condition checking
a = int(input("Enter your age : "))

if(a >= 18):
    print("You are above the age of consent !")
elif(a < 0):
    print("You are entering invalid age !")
else:
    print("You are below the age of 18")

print("End of program")
```

## 🎯 Practice Problems

### 1. Greatest Number Finder

```python
# Find largest among four numbers
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

if(a > b and a > c and a > d):
    print("a is largest of 4")
elif(b > a and b > c and b > d):
    print("b is largest of 4")
elif(c > b and c > a and c > d):
    print("c is largest of 4")
elif(d > b and d > c and d > a):
    print("d is largest of 4")
```

### 2. Student Grade Calculator

```python
# Calculate pass/fail status
marks1 = int(input("Enter marks of subject 1 : "))
marks2 = int(input("Enter marks of subject 2 : "))
marks3 = int(input("Enter marks of subject 3 : "))

total_percentage = ((marks1 + marks2 + marks3)/300)*100

if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print(f"Congratulations! You passed with {total_percentage}%!")
else:
    print(f"Failed with {total_percentage}%. Try again!")
```

### 3. Spam Detector

```python
# Detect spam messages
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter the message : ")

if((p1 in message) or (p2 in message) or (p3 in message)):
    print("This message is a spam !")
else:
    print("Comment is not a spam")
```

### 4. Username Validator

```python
# Check username length
username = input("Enter Username : ")

if(len(username) < 10):
    print("Username is of length less than 10 characters")
else:
    print("Username is greater or equal to 10 characters")
```

### 5. List Membership Checker

```python
# Check name in list
l = ['Shashwat', "Risha", "Sushant", "DJ"]
name = input("Enter your name : ")

if(name in l):
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")
```

### 6. Grade Assigner

```python
# Grade assignment based on marks
marks = int(input("Enter your marks: "))

if(marks <= 100 and marks >= 90):
    grade = "Ex"
elif(marks < 90 and marks >= 80):
    grade = "A"
elif(marks < 80 and marks >= 70):
    grade = "B"
elif(marks < 70 and marks >= 60):
    grade = "C"
elif(marks < 60 and marks >= 50):
    grade = "D"
elif(marks < 50):
    grade = "F"

print(f"Your grade is {grade}")
```

### 7. Case-Insensitive Search

```python
# Case-insensitive string search
post = input("Enter the post: ")

if("Shashwat".lower() in post.lower()):
    print("This post is talking about Shashwat")
else:
    print("This post is not talking about Shashwat")
```

## 📚 Advanced Topics

### Important Rules and Guidelines

1. **Indentation Rules**

   - Consistent indentation (4 spaces recommended)
   - Required for defining code blocks
   - Critical for proper execution

2. **If-Elif-Else Structure**

   ```python
   if condition1:
       # code block
   elif condition2:
       # code block
   else:
       # code block
   ```

3. **Best Practices**

   - Validate all user inputs
   - Keep conditions simple and readable
   - Use meaningful variable names
   - Add comments for complex logic

4. **Common Pitfalls**
   - Using `=` instead of `==` for comparison
   - Forgetting proper indentation
   - Not handling all possible cases
   - Overcomplicating conditions
