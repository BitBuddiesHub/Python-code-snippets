from PIL import Image

"""
pip install pillow
"""


# 打开文件，模式默认为文本模式，文件被假定为包含了可读的文本（如UTF-8编码的字符）。
# with open('example.txt', 't') as file:
with open('example.txt') as file:
    data = file.read()
    print(data)

# 新建文件进行写入，如果文件已存在则报错
try:
    with open('newfile.txt', 'x') as file:
        file.write("Hello World!")
except FileExistsError:
    print("File already exists.")

# 以二进制模式读取文件，每个字节都原样保留。
with open('example.txt', 'rb') as file:
    data = file.read()
    print(data)


# 打开文件进行更新（可读可写）
with open('example.txt', 'r+') as file:
    file.write("Adding new line.\n")
    file.seek(0)
    # file.seek(offset, whence)
    data = file.read()
    print(data)


# 以只读方式打开文件
with open('example.txt', 'r') as file:
    file.write("Adding new line.\n") # io.UnsupportedOperation: not writable
    data = file.read()
    print(data)


# 以二进制格式打开一个文件用于只读
with open('example.txt', 'rb') as file:
    data = file.read()
    print(data)


# 打开一个文件用于读写
with open('example.txt', 'r+') as file:
    file.write("New content.\n")
    file.seek(0)
    data = file.read()
    print(data)


# 以二进制格式打开一个文件用于读写
with open('example.txt', 'rb+') as file:
    file.write(b"Binary content.\n")
    file.seek(0)
    data = file.read()
    print(data)


# 打开一个文件只用于写入，如果文件存在则覆盖
with open('example.txt', 'w') as file:
    file.write("Overwrite existing content.\n")


# 以二进制格式打开一个文件只用于写入，覆盖已存在的内容
with open('example.txt', 'wb') as file:
    file.write(b"Binary overwrite.\n")


# 打开一个文件用于读写，如果文件存在则覆盖
with open('example.txt', 'w+') as file:
    file.write("Overwrite and read.\n")
    file.seek(0)
    data = file.read()
    print(data)


# 以二进制格式打开一个文件用于读写，覆盖已存在的内容
with open('example.txt', 'wb+') as file:
    file.write(b"Binary overwrite and read.\n")
    file.seek(0)
    data = file.read()
    print(data)


# 打开一个文件用于追加
with open('example.txt', 'a') as file:
    file.write("Appending new content.\n")


# 以二进制格式打开一个文件用于追加
with open('example.txt', 'ab') as file:
    file.write(b"Binary append.\n")


# 打开一个文件用于读写，追加模式
with open('example.txt', 'a+') as file:
    file.write("Append and read.\n")
    file.seek(0)
    data = file.read()
    print(data)


# 以二进制格式打开一个文件用于追加读写
with open('example.txt', 'ab+') as file:
    file.write(b"Binary append and read.\n")
    file.seek(0)
    data = file.read()
    print(data)


image = Image.open('hcj5.jpg')
# print(image)
image.show()


print("---------------------------")


file = open('example.txt', 'r')
data = file.read()
print(data)
file.close()  # 关闭文件



file = open('example.txt', 'w')
file.write('Hello world!')
file.flush()  # 刷新内部缓冲区
file.close()


file = open('example.txt', 'r')
# 0：标准输入（stdin）
# 1：标准输出（stdout）
# 2：标准错误（stderr）
print(file.fileno())  # 打印文件描述符
file.close()



file = open('example.txt', 'r')
print(file.isatty())  # 检查是否连接到终端
file.close()


file = open('example.txt', 'r')
print(file.read(10))  # 读取前10个字节
file.close()


# 打开文件
with open('example.txt', 'r') as file:
    first_line = file.readline()  # 读取第一行
    second_line = file.readline()  # 读取第二行

# 打印读取的内容
print("第一行:", first_line)
print("第二行:", second_line)


file = open('example.txt', 'r')
print(file.readlines())  # 读取所有行
file.close()


file = open('example.txt', 'r+')
file.seek(5)  # 移动到文件的第6个字节
print(file.read(1))  # 读取一个字符
file.close()


file = open('example.txt', 'r')
file.seek(5)
print(file.tell())  # 打印当前位置
file.close()


file = open('example.txt', 'r+')
file.truncate(10)  # 截断文件到前10个字节
file.close()


file = open('example.txt', 'w')
length = file.write('Hello world!')  # 写入字符串
print(length)  # 打印写入的字符数
file.close()

lines = ['Hello\n', 'world\n']
file = open('example.txt', 'w')
file.writelines(lines)  # 写入多行
file.close()
