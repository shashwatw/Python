# write a program to format the following letter using escape sequence characters
name = input("Enter name : ")
company = input("Enter company : ")
letter = f"Dear {name},\n\tYou cracked {company}.\nCongratulations!"
print(letter)