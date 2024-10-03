# Python Lists and Tuples

A comprehensive guide to Python Lists and Tuples, including their methods, operations, and practical examples.

## 📋 Table of Contents

- [Lists](#lists)
- [List Methods](#list-methods)
- [Tuples](#tuples)
- [Tuple Operations](#tuple-operations)
- [Practice Problems](#practice-problems)
- [Key Differences](#key-differences)
- [Important Rules & Notes](#important-rules--notes)

## 📝 Lists

Lists are mutable sequences that can store multiple values of different data types:

```python
# List Creation and Basic Operations
friends = ["Apple", "Oranges", 5, 345.06, False, "Shashwat"]
print(friends[0])        # Accessing elements
friends[1] = "Cherry"    # Modifying elements
print(friends[1:4])      # Slicing
```

## 🛠️ List Methods

```python
l1 = [10, 4, 7, 3, 2, 9, 1, 8]

# Common List Methods
l1.append(5)          # Add element at end
l1.sort()             # Sort list in-place
l1.reverse()          # Reverse list in-place
l1.insert(2, 3333)    # Insert at specific index
l1.pop(3)             # Remove and return element at index
l1.remove(10)         # Remove first occurrence of value
```

## 📦 Tuples

Tuples are immutable sequences that can store multiple values:

```python
# Tuple Creation
empty_tuple = ()
single_element = (1,)  # Note the comma
mixed_tuple = (1, 2, 5, 6, False, "Shashwat")

# Basic Operations
print(type(mixed_tuple))
print(mixed_tuple)
```

## 🔧 Tuple Operations

```python
tuple_a = (1, 2, 5, 6, 1, 5, False, "Shashwat")

# Common Tuple Operations
print(tuple_a.count(5))          # Count occurrences
print(tuple_a.index(2))          # Find first index
print((1, 2, 3) * 3)            # Repeat tuple
print(len(tuple_a))             # Get length
print(2 in tuple_a)             # Check membership
print(min((1, 2, 3)))          # Find minimum
print(max((1, 2, 3)))          # Find maximum

# Tuple Unpacking
p, q, r = (1, 2, 3)
```

## 💻 Practice Problems

### 1. Fruit List Creator

```python
fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)
print(fruits)
```

### 2. Student Marks Sorter

Method 1

```python
students = []

student1 = int(input("Enter Marks"))
students.append(student1)
student2 = int(input("Enter Marks"))
students.append(student2)
student3 = int(input("Enter Marks"))
students.append(student3)
student4 = int(input("Enter Marks"))
students.append(student4)
student5 = int(input("Enter Marks"))
students.append(student5)
student6 = int(input("Enter Marks"))
students.append(student6)

students.sort()
print(students)
```

Method 2 (using loop)

```python
students = []
for i in range(6):
    marks = int(input("Enter Marks: "))
    students.append(marks)
students.sort()
print(students)
```

### 3. Tuple Immutability Test

```python
a = (34, 211, "Shashwat")
# a[2] = "Change"  # This will raise TypeError
```

### 4. List Sum Calculator

```python
l = [3, 3, 5, 1]
print(sum(l))
```

### 5. Zero Counter

```python
a = (7, 0, 8, 0, 0, 9)
print("Number of zeroes:", a.count(0))
```

## 📊 Key Differences

### Lists vs Tuples

| Feature     | Lists                        | Tuples                       |
| ----------- | ---------------------------- | ---------------------------- |
| Mutability  | Mutable                      | Immutable                    |
| Syntax      | `[]`                         | `()`                         |
| Methods     | Many (append, sort, etc.)    | Few (count, index)           |
| Performance | Slower                       | Faster                       |
| Use Case    | Collection that might change | Collection that won't change |

## 📝 Important Rules & Notes

### List Rules

1. Lists are mutable - elements can be changed
2. Lists can contain elements of different types
3. Lists can be sliced like strings
4. List methods modify the list in-place
5. Lists are ordered sequences

### Tuple Rules

1. Tuples are immutable - cannot be changed after creation
2. Single element tuples need a trailing comma
3. Tuples can be used as dictionary keys (unlike lists)
4. Tuple operations create new tuples
5. Tuples are faster than lists for iteration

## 🚫 Common Mistakes to Avoid

1. Forgetting comma in single-element tuples
2. Trying to modify tuples
3. Using wrong method names (append vs. extend)
4. Forgetting that list methods modify in-place
5. Not considering performance implications

## 🔍 Advanced Tips

1. Use tuple unpacking for multiple assignments
2. Consider tuples for data that shouldn't change
3. Use list comprehensions for creating lists
4. Leverage built-in functions like `map()` and `filter()`
5. Use `enumerate()` for index access in loops
