# Python String Operations & Manipulations

A comprehensive guide to Python strings, including string operations, methods, escape sequences, and practical examples.

## 📋 Table of Contents

- [String Basics](#string-basics)
- [String Slicing](#string-slicing)
- [String Methods](#string-methods)
- [Escape Sequences](#escape-sequences)
- [Practice Problems](#practice-problems)
- [Important Rules & Notes](#important-rules--notes)

## 🔤 String Basics

Strings in Python are immutable sequences of characters:

```python
name = "Shashwat"
nameLength = len(name)    # Get string length
character1 = name[1]      # Access individual character

print(nameLength)         # Output: 8
print(character1)         # Output: h
```

## ✂️ String Slicing

### Basic Slicing

```python
name = "Shashwat"
print(name[0:3])    # Output: Sha
```

### Negative Slicing

```python
#  S  H  A  S  H  W  A  T
#  0  1  2  3  4  5  6  7
# -8 -7 -6 -5 -4 -3 -2 -1

name = "Shashwat"
print(name[-6:-1])  # Output: ashwa
print(name[2:7])    # Output: ashwa
```

### Default Indices

```python
print(name[:5])     # From start to index 5
print(name[1:])     # From index 1 to end
```

### Skip Value Slicing

```python
print(name[0:8:2])  # Skip every second character
```

## 🛠️ String Methods

```python
name = "shashwat wankhedekar"

print(len(name))                    # Length
print(name.endswith("wat"))         # Check ending
print(name.startswith("sha"))       # Check starting
print(name.capitalize())            # Capitalize first letter
print(name.title())                 # Capitalize each word
print(name.find("wankhedekar"))     # Find substring
print(name.replace("wankhedekar", "sir"))  # Replace substring
```

## 🔠 Escape Sequences

```python
text = "Line 1\nLine 2\tTabbed\n\"Quoted\""
print(text)

# Common Escape Sequences:
# \n - Newline
# \t - Tab
# \" - Double quote
# \' - Single quote
# \\ - Backslash
```

## 💻 Practice Problems

### 1. Greeting Generator

```python
name = input("Enter your name: ")
print(f"Good Afternoon {name}!")  # Using f-strings
```

### 2. Template Letter

```python
letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Shashwat")
           .replace("<|Date|>", "2 October 2024"))
```

### 3. Double Space Detection

```python
text = "abc def  ghi"
print(text.find("  "))
```

### 4. Space Normalization

```python
text = "abc  def  ghi klm no"
print(text.replace("  ", " "))
```

### 5. Formatted Letter

```python
name = input("Enter name: ")
company = input("Enter company: ")
letter = f"Dear {name},\n\tYou cracked {company}.\nCongratulations!"
print(letter)
```

## 📝 Important Rules & Notes

### String Immutability

1. Strings are immutable in Python - cannot be changed after creation
2. All string methods return new strings
3. Original string remains unchanged after operations

### Slicing Rules

1. Start index is inclusive
2. End index is exclusive
3. Default start index is 0
4. Default end index is length of string
5. Negative indices count from end of string

### Best Practices

1. Use f-strings for string formatting
2. Prefer `str.replace()` over manual character replacement
3. Use appropriate escape sequences for formatting
4. Consider string methods over manual implementations
5. Use meaningful variable names for strings

## 🚫 Common Mistakes to Avoid

1. Trying to modify strings directly
2. Forgetting that slice end index is exclusive
3. Not handling string immutability properly
4. Incorrect use of escape sequences
5. Mixing string concatenation methods

## 🔍 Advanced Tips

1. Use `str.join()` for efficient string concatenation
2. Leverage f-strings for complex formatting
3. Consider using raw strings (r"string") for regex
4. Use string methods instead of loop operations
5. Understand string interning for optimization
