class Employee:
    language = "Py"
    salary = 1200000

shashwat = Employee()
shashwat.name = "Shashwat"
print(shashwat.name, shashwat.language, shashwat.salary)

rohan = Employee()
rohan.name = "Rohan Robin"
print(rohan.name, rohan.language, rohan.salary)

# Here name is instance attribute and salary and lang are class attributes as they directly belong to the class
# Instance attributes always take preference over class attributes while assignment and retrieval