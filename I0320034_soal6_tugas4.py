x = 4       # 4 = 0000 0100
y = 11      # 11 = 0000 1011

# a
a = x | y
print("a. 4|11 =", a)

# b
b = x >> y
print("b. 4>>11 =", b)

# c
c = x ^ y
print("c. 4^11 =", c)

# d
d = ~x
print("d. ~4 =", d)

# e
e = y & x
print("e. 11&4 =", e)
