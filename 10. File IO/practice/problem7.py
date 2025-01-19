# read from problem6_log.txt that in which line "python" is written
with open("problem6_log.txt", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes! python is present in the file on line {lineno}")
        break
    lineno += 1
# This else will only be executed if whole for loop is executed. In case of break else won't execute
else:
    print(f"No!, python is not present in the file")