Name = input("请输入你的名字:")
Age = int(input("请输入你的年龄:"))
print("你好," + Name)

print("我的名字是{Name}")
print(f"我的名字是{Name}")

print("我的名字是 %s 并且我的年龄是 %i 岁" % (Name, Age))


height = 175.5

print("My height is %.2f cm." % height)

number = 123456.789

print("Scientific notation: %e" % number)

number = 255

print("Hexadecimal: %x" % number)
print("Octal: %o" % number)

char = 'A'
percentage = 85.5

print("Character: %c" % char)
print("You scored %f%% on your test." % percentage)

width = 10
number = 3.14159

print("Right aligned: [%10s]" % ("right",))
print("Left aligned: [%-10s]" % ("left",))
print("Number with fixed width: [%*.*f]" % (width, 3, number))
