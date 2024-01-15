str = '123456789'
xb   ='012345678' # 下标

print(len(str)) # 输出字符串的长度

print(str) # 输出字符串
print(str[0]) # 输出字符串中的第一个字符
print(str[2:5]) # 输出从第三个开始到第六个的字符（不包括）
print(str[0:-1]) # 输出第一个到倒数第二个的所有字符 等价于 print(str[0:len(str)-1])
print(str[1:5:2]) # 输出从第二个开始到第六个的间隔为2的字符 
print(str * 2) # 输出字符串两次
print(str + str) # 连接字符串
print(str + " " + str) # 连接字符串

str_2 = "yjs"
print(str_2.upper()) # 将字符串转为大写
# print(int(str_2)) # 将字符串转为整数 ValueError: invalid literal for int() with base 10: 'yjs'

x = 'x'
ascii_value = ord(x)
print(ascii_value)

a = 97
char_from_ascii = chr(a)
print(char_from_ascii)

"""
ascii_value_2 = ord(str_2)
print(ascii_value_2) # ord() expected a character, but string of length 3 found
"""

str_3 = "Hello World!"
print('Hello \nWorld')
print(r'Hello \nWorld') # 原样输出字符串