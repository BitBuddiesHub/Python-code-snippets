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