"""
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
"""

x = 10
if x > 5:
    print("x大于5")
else:
    print("x小于等于5")
    
a = 30
if a > 10:
    print("a大于10")
    if a > 20:
        print("a大于20")
    else:
        print("a不大于20")
else:
    print("a不大于10")
    

        
b , c=5, 15
if b > 10 and c > 10:
    print("b大于10并且c大于10")
    if a > 20 or c > 10:
        print("a大于20")
    else:
        print("a不大于20")
        
list = [1,2,3,4,5]
if 3 in list:
    print("3在列表中")
else:
    print("3不在列表中")

d = 7
result = "大于5" if d > 5 else "小于等于5"
# a if condition else b
print(result)

"""
match subject:
    case pattern_1:
        statement_block_1
    case pattern_2:
        statement_block_2
    case pattern_3:
        statement_block_3
    case _:
        statement_block_4
"""


e = 30
match e:
    case _ if e < 10:
        print("e小于10")
    case _ if 10 <= e <= 20:
        print("e在10到20之间")
    case _ if e > 20:
        print("e大于20")

def handle_data(data):
    if type(data) == int:
        print("data is int")
    elif type(data) == str:
        print("data is str")
    elif type(data) == list:
        print("data is list")
    elif type(data) == dict:
        print("data is dict")
    else:
        print("data is unknown")


def handle_data_2(data):
    match data:
        case _ if isinstance(data, int):
            print("data is int")
        case _ if isinstance(data, str):
            print("data is str")
        case _ if isinstance(data, list):
            print("data is list")
        case _ if isinstance(data, dict):
            print("data is dict")
        case _:
            print("data is unknown")

handle_data(10)
handle_data("smg: I Love BYX")
handle_data([1,2,3])
handle_data({"name":"smg", "age":17 , "is_single": False})

handle_data_2(10)
handle_data_2("smg: I Love BYX")
handle_data_2([1,2,3])
handle_data_2({"name":"smg", "age":17 , "is_single": False})
    
    