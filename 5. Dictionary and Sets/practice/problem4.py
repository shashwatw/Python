# What will be length of set with following elements

s = set()

s.add(20)
s.add(20.0)
s.add("20")

print(s)

# length comes out as 2 with {'20', 20} as output

# This is because python checks values but not datatypes so,
# 10 == 10.0 ----> True