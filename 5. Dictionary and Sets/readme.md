# Python Dictionaries & Sets

A comprehensive guide to Python Dictionaries and Sets, including their properties, methods, and practical examples.

## 📋 Table of Contents

- [Dictionaries](#dictionaries)
- [Dictionary Methods](#dictionary-methods)
- [Sets](#sets)
- [Set Operations](#set-operations)
- [Practice Problems](#practice-problems)
- [Key Differences](#key-differences)
- [Important Rules](#important-rules)

## 📚 Dictionaries

```python
# Key-value pairs collection
marks = {
    "Shashwat": 100,
    "Sahil": 56,
    "Ramesh": 23,
    list: [100, 89, 76, 88]
}
```

### Properties

- Unordered collection
- Mutable (can be modified)
- Keys must be unique and immutable
- O(1) lookup time complexity
- Cannot have duplicate keys

## 🔧 Dictionary Methods

```python
marks = {"Shashwat": 100, "Sahil": 56}

# Common Operations
print(marks.items())     # Get key-value pairs
print(marks.keys())      # Get all keys
print(marks.values())    # Get all values
marks.update({"New": 99})  # Add/Update items
print(marks.get("Key", "Default"))  # Safe get
marks.pop("Key", "Default")  # Remove key
marks.popitem()          # Remove last item (LIFO)
```

## 🎯 Sets

```python
# Unique elements collection
empty_set = set()    # Create empty set
my_set = {1, 5, 32}  # Create with values
```

### Properties

- Unordered collection
- Unindexed
- Immutable elements only
- No duplicates allowed
- Mutable (can add/remove elements)

## ⚡ Set Operations

```python
s1 = {1, 45, 6, 78}
s2 = {7, 8, 1, 78}

# Basic Operations
print(s1.union(s2))           # All unique elements
print(s1.intersection(s2))    # Common elements
s1.add(566)                   # Add element
s1.remove(45)                 # Remove element
print(s1.issubset(s2))       # Check subset
print(s1.issuperset(s2))     # Check superset
```

## 💡 Practice Problems

### 1. Hindi-English Dictionary

Create a translation dictionary with lookup functionality.

```python
words = {
    "kursi": "Chair",
    "billi": "cat",
    "dabba": "box"
}

word = input("Enter the Hindi word: ")
print(words.get(word, "Word not found!"))
```

**Learning Point**: Safe dictionary access using `.get()`

### 2. Unique Number Collection

Input eight numbers and display unique values using a set.

(i) Method 1 (Without Loops)

```python
st = set() # initialise empty set

num1 = int(input("Enter number 1 : "))
st.add(num1)
num2 = int(input("Enter number 3 : "))
st.add(num2)
num3 = int(input("Enter number 3 : "))
st.add(num3)
num4 = int(input("Enter number 4 : "))
st.add(num4)
num5 = int(input("Enter number 5 : "))
st.add(num5)
num6 = int(input("Enter number 6 : "))
st.add(num6)
num7 = int(input("Enter number 7 : "))
st.add(num7)
num8 = int(input("Enter number 8 : "))
st.add(num8)

print(st)
```

(ii) Method 2 (Using Loops)

```python
numbers = set()
for i in range(8):
    num = int(input(f"Enter number {i+1}: "))
    numbers.add(num)
print("Unique numbers:", numbers)
```

**Learning Point**: Automatic duplicate removal with sets

### 3. Set Type Coexistence

Testing different types in a set.

```python
mixed_set = set()
mixed_set.add(18)      # Integer
mixed_set.add("18")    # String
print(mixed_set)       # Both coexist: {18, '18'}
```

**Learning Point**: Sets can contain different types if they're immutable

### 4. Number Type Handling

Understanding how sets handle similar values of different types.

```python
number_set = set()
number_set.add(20)     # Integer
number_set.add(20.0)   # Float
number_set.add("20")   # String
print(number_set)      # Output: {'20', 20}
```

**Learning Point**: Python considers `20` and `20.0` as equal values

### 5. Empty Collection Type

Understanding the difference between empty dictionaries and sets.

```python
empty_dict = {}        # Creates empty dictionary
empty_set = set()      # Creates empty set
print(type(empty_dict))  #
print(type(empty_set))   #
```

**Learning Point**: Empty curly braces create a dictionary, not a set

### 6. Favorite Language Dictionary

Create a dictionary of names and favorite programming languages.

(i) Method 1 (Without Loops)

```python
dictionary = {}

name1 = input("Enter your name : ")
lang1 = input("Enter your fav language : ")
dictionary.update({name1 : lang1})

name2 = input("Enter your name : ")
lang2 = input("Enter your fav language : ")
dictionary.update({name2 : lang2})

name3 = input("Enter your name : ")
lang3 = input("Enter your fav language : ")
dictionary.update({name3 : lang3})

name4 = input("Enter your name : ")
lang4 = input("Enter your fav language : ")
dictionary.update({name4 : lang4})

print(dictionary)
```

(ii) Method 2 (Using Loops)

```python
languages = {}
for i in range(4):
    name = input(f"Friend {i+1} name: ")
    lang = input(f"Favorite language: ")
    languages[name] = lang  # or use update()
print(languages)
```

**Learning Point**: Dictionary updates and unique keys

### 7. Set Mutability Rules

Understanding what can and cannot be stored in sets.

```python
# This will raise TypeError
try:
    invalid_set = {8, 7, 12, "Shashwat", [1, 2]}
except TypeError as e:
    print("Cannot add list to set - lists are mutable")

# This works
valid_set = {8, 7, 12, "Shashwat", (1, 2)}  # Using tuple
```

**Learning Point**: Sets can only contain immutable (hashable) elements

## 🔑 Key Differences

### Dictionary vs Set

| Feature    | Dictionary        | Set                |
| ---------- | ----------------- | ------------------ |
| Purpose    | Key-value storage | Unique elements    |
| Syntax     | `{}` with `:`     | `{}` or `set()`    |
| Ordering   | Unordered         | Unordered          |
| Duplicates | No duplicate keys | No duplicates      |
| Access     | By key            | No direct access   |
| Use Case   | Mapping data      | Unique collections |

## ⚠️ Important Rules

### Dictionary Rules

1. Keys must be immutable (str, int, tuple)
2. Values can be of any type
3. `dict.get()` is safer than `[]` access
4. O(1) lookup time complexity
5. Keys must be unique

### Set Rules

1. Cannot contain mutable elements (no lists)
2. No indexing available
3. Perfect for removing duplicates
4. All elements must be hashable
5. Cannot modify elements in place

## 🚫 Common Mistakes

1. Using `{}` for empty set (creates dict)
2. Adding mutable objects to sets
3. Assuming dictionaries are ordered (< Python 3.7)
4. Not using `.get()` for safe dictionary access
5. Modifying items during iteration

## 🔍 Quick Tips

1. Use `dict.get()` with default values
2. Convert lists to sets for unique elements
3. Use set operations for data comparison
4. Dictionary comprehension for creation
5. Check membership using `in` operator

## 🛠️ Setup

```python
# Quick Start
empty_dict = {}          # Empty dictionary
empty_set = set()        # Empty set (not {})
```
