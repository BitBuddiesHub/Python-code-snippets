# x = 1/0  ZeroDivisionError: division by zero
# 4 + y*3  NameError: name 'y' is not defined
# "2" + 2  TypeError: can only concatenate str (not "int") to str

while True:
    try:
        x = int(input("Please enter a number: "))
        print ("you input:" , x)
    except ValueError as e:
        print("Oops!  That was no valid number.  Try again...")
        print("Your ValueError is:" , e)
    except NameError as e:
        print("Oops!  That was no valid name.  Try again...")
        print("Your NameError is:" , e)
    except:
        print("Unexpected error:", sys.exc_info()[0]) # 获取当前异常的信息。这通常用于调试目的，以了解发生了哪种类型的异常。
        raise
        # raise [Exception [, args [, traceback]]]
    finally:
        print("I give up")
        
"""
def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a/b

try:
    result = divide(10,0)
except ZeroDivisionError as error:
    print("Error message:", error)
"""