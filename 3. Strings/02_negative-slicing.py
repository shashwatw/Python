name = "Shashwat"

print(name[0:3])

print(name[-6:-1]) # convert negative to corresponding positive indexes from below method
#  S  H  A  S  H  W   A   T
#  0  1  2  3  4  5   6   7
# -8 -7 -6 -5 -4 -3  -2  -1
print(name[2:7])

print(name[:5]) # If : ke pehle kuch nhi likha means it is 0
print(name[1:]) # If : ke baad kuch nhi likha means it is len-1

#* Slicing with skip value
print(name[0 : 8 : 2]) # means 0 to last index(excluding) and with jumps/skips of 2

