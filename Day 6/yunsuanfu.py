a = 10
b = 20
print (a+b)
print (a-b)
print (a*b)
print (a/b)
print (a%b)
print (a**b)
print (a//b)

c = 10
c += 10
# c = c + 10

n = 10
if n > 5:
    print(n)

# 海象运算符

if (n := 10) > 5:
    print (n)
    

d = 60
# 0011 1100
e = 13
# 0000 1101
# & 按位与运算符
print(d&e)
# d   0011 1100
# e   0000 1101
# d&e 0000 1100 12

# | 按位或运算符
print(d|e)
# d   0011 1100
# e   0000 1101
# d|e 0011 1101 61

# ^ 按位异或运算符
print(d^e)
# d   0011 1100
# e   0000 1101
# d^e 0011 0001 49

# ~ 按位取反运算符
print(~d)
# d   0011 1100
# ~d  1100 0011 -49

# << 左移运算符
# >> 右移运算符

""" and or not """

""" in not in """

list = ["smg","yjs","cyq"]
if "smg" in list:
    print("yes")
else:
    print("no")

if "wzr" not in list:
    print("查无此人")
    
"""is is not"""

a = "smg"
b = "wzr"
if (a is b):
    print("yes")
else:
    print("no")
    
a = [1,2,3]
b = a
print (b is a) # True
print (b == a) # True

b = a[:]
print (b is a) # False
print (b == a) # True

