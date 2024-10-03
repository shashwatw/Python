# Python Programming Basics - Chapter 1: Introduction to Python

Welcome to Chapter 1 of the Python Programming handbook! This chapter introduces fundamental concepts and basic operations in Python, along with practical examples and exercises.

## 📋 Table of Contents

- [Introduction](#introduction)
- [Basic Operations](#basic-operations)
- [Practice Tasks](#practice-tasks)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)

## 🚀 Introduction

This chapter covers the basics of Python programming, including:

- Printing text to console
- Comments in Python
- Working with external libraries
- Basic file operations

## 💻 Basic Operations

### Hello World

```python
print("Hello World")
```

### Comments

```python
# This is a single-line comment

"""
This is how a multiline
comment looks like
"""
```

### Using External Libraries

```python
import pyjokes
jokes = pyjokes.get_joke()
print(jokes)
```

## 🎯 Practice Tasks

### Task 1: File System Operations

```python
import os

# Specify the directory path
directory_path = '/'

# List all files and directories
contents = os.listdir(directory_path)
print(contents)
```

### Task 2: Text-to-Speech

```python
import pyttsx3

engine = pyttsx3.init()
engine.say("Please hold my cup of tea")
engine.runAndWait()
```

### Task 3: Multiline String Printing

```python
print('''
Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!
''')
```

## ⚙️ Requirements

To run the code in this chapter, you'll need:

- Python 3.x
- pyjokes library
- pyttsx3 library
- os module (built-in)

## 🛠️ Setup Instructions

1. Clone this repository:

```bash
git clone https://github.com/yourusername/python-basics.git
cd python-basics
```

2. Install Python from [python.org](https://python.org)

3. Install required packages:

```bash
pip install pyjokes pyttsx3
```

## 📝 Notes

> - Make sure to handle file system permissions when using the `os` module
> - Text-to-speech functionality requires proper audio output configuration
> - External libraries might need additional setup based on your operating system
