# Celsius to Fahrenheit

# c/5 = (f - 32)/9
# c = s*(f -32)/9

def fah_to_cel(f):
    return 5*(f-32)/9

f = int(input("Enter Temnperature in Fahrenheit: "))
c = fah_to_cel(f)
print(f"{round(c, 2)}° C")