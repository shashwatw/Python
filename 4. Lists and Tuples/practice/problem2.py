# Write a program to accept mar s of 6 students and display them in a sorted manner.

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