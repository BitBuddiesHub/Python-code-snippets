# 定义一个名为 Student 的类
class Student:
    
    student_num = 0 # 类的属性，用于记录学生总数 (类变量)
    
    # 类的构造函数，用于初始化学生实例的属性
    def __init__(self, name, age, grade):
        self.name = name  # 学生的姓名
        self.age = age    # 学生的年龄
        self.grade = grade  # 学生的年级
        Student.student_num += 1 # 学生总数加1 (建议统一使用类名)
        
        '''当你使用 Student.student_num += 1，你直接操作了类变量 student_num。这意味着每次调用 __init__ 方法时，都会
        增加这个类变量的值。因此，对于每个创建的学生实例，Student.student_num 都会递增，从而正确地记录了总的学生数。
        '''
        
        # self.student_num += 1 # wait...
        
        ''' 当你使用 self.student_num += 1，实际上你在每个学生实例的 __init__ 方法中创建了一个新的实例变量 student_num，
        并且将其设为 1。这意味着每次创建新的学生实例时，这个实例的 student_num 都会从类变量 Student.student_num（默认值是
        0，除非你在其他地方修改它）拷贝一份并增加1，但这个增加不会影响类变量本身，所以 Student.student_num 保持不变。
        '''
    @classmethod
    def add_student(cls, name, age, grade):
        cls.student_num += 1
        return cls(name, age, grade)
    
    @classmethod
    def add_bulk_students(cls, add_num):
        for i in range(add_num):
            cls.student_num += 1;
    
    @classmethod
    def from_string(cls, student_str):
        name, age, grade = student_str.split(",")
        return cls(name, int(age), grade)
    
    @staticmethod
    def name_length(name):
        return len(name)

# 创建一个学生实例 s1，姓名为"John"，年龄为16岁，年级为"10th"
s1 = Student("John", 16, "10th")

# 创建另一个学生实例 s2，姓名为"Jane"，年龄为17岁，年级为"11th"
s2 = Student("Jane", 17, "11th")

# 使用类方法创建一个学生实例 s3，姓名为"John"，年龄为18岁，年级为"12th"
s3 = Student.from_string("John,18,12th")

print(f"Student 1: {s1.name}, {s1.age} years old, {s1.grade}")
print(f'Student.student_num: {Student.student_num}')

print(f's2.name: {s2.name}, s2.name.length: {Student.name_length(s2.name)}') # 这里是调用静态方法，静态方法不需要实例化，直接用类名调用



'''在Python中，类变量、类方法和静态方法是面向对象编程中非常重要的概念。

### 1. 类变量
类变量是定义在类中的变量，它们被该类的所有实例共享。这意味着类变量的一个副本不属于任何单个实例，而是属于类本身。当一个实例修改了类变量的值时，这个修改对所有其他实例都是可见的。类变量通常用于存储类级别的属性，比如在你之前的例子中，`student_num` 用于跟踪创建的学生总数。

### 2. 类方法
类方法是定义在类中的方法，它使用装饰器 `@classmethod` 标记，并且它的第一个参数是类本身，通常命名为 `cls`。类方法可以访问和修改类变量，也可以调用其他的类方法。它不能访问类的实例变量，因为它不绑定到任何实例上。类方法通常用于执行与整个类相关的操作，而不是与特定实例相关的操作。

```python
class MyClass:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1
```

### 3. 静态方法
静态方法是另一种定义在类中的方法，使用装饰器 `@staticmethod` 标记。静态方法不接受类或实例的隐式第一个参数（即没有 `self` 或 `cls` 参数）。它基本上就是一个在类定义内部的普通函数，用于执行不需要类或实例数据的操作。静态方法不能访问类或实例的任何属性（除非显式提供）。

```python
class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method.")
```
这三种元素（类变量、类方法和静态方法）在面向对象编程中提供了结构和模块化的方法来管理数据和行为，使得代码更加组织化和可复用。
'''