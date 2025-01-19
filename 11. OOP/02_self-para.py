class Employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    # def greet(self):
    #     print("Good Morning")
            # or
    @staticmethod # decorator to tell it does not take any param
    def greet():
        print("Good Day")

shashwat = Employee()
# print(shashwat.language, shashwat.salary)

shashwat.getInfo() # --> Employee.getInfo(shashwat) both are same
# That's why we usually give it a "self" parameter
shashwat.greet() # For plain string also self parameter is necessary