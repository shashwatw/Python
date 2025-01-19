f = open("file.txt")

# To print altogether -->
# lines = f.readlines()
# print(lines, type(lines))

# To print linewise strings (without loop)-->
# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5 == "")

# To print linewise strings (with loop)-->
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()