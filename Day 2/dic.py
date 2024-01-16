# d = {key1 : value, key2 : value2 , key3 : value3}

personal_information = {"name" : "yjs" , "age" : 18 , "height" : 1.68, "is_single" : True}

print(personal_information)
print("length of personal_information is ", len(personal_information))
print(type(personal_information))

print("His name is", personal_information["name"])
print("He is single", personal_information["is_single"])

# print("he live in ", personal_information["address"]) KeyError: 'address'

personal_information["is_single"] = False
print("He is single", personal_information["is_single"])
personal_information["address"] = "Shanghai"
print("he live in", personal_information["address"])

del personal_information["address"]
# print("he live in ", personal_information["address"]) KeyError: 'address'

"""
删除词典
personal_information.clear()
del personal_information
"""

personal_information_2 = {"name" : "qhw" , "name": "zwz"}
print(personal_information_2["name"])  #同一个键不能出现两次，如果出现两次或者多次，后一个赋值的值会被记住

print(len(personal_information)) #length
print(str(personal_information)) #str
print(type(personal_information)) #type

dict.copy(personal_information) #copy
print("a copy version of personal_information: ", dict.copy(personal_information))

print("----------------------------")

dict1 ={"name":"yjs", "age":18, "height":1.68, "is_single":True, "friends":["qhw","zwz","cyq"]}

dict2 = dict1         # 浅拷贝：引用对象
dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，子对象引用

dict1["is_single"] = False
dict1["friends"].remove("qhw")

print(dict1)
print(dict2)
print(dict3)

print("----------------------------")

seq = ('name', 'age', 'height', 'is_single', 'friends')
# dict.fromkeys(seq[, value])
dict4 = dict.fromkeys(seq)
print(dict4)
print("The new dict is:", dict4)

dict4 = dict.fromkeys(seq, "default")
print("The new dict is:", dict4)

print("----------------------------")

# dict.get(key[, value]) 
cities = {'BJ': 'Beijing', 'SH': 'Shanghai', 'GZ': 'Guangzhou', 'SZ': 'Shenzhen'}
print("BJ is", cities.get('BJ', "I don't know")) # 有键值，所以默认值无效
# print("BJ is",cities["BJ"])
print("CQ is", cities.get('CQ'))
print("HK is", cities.get('HK', "I don't know")) # 无键值，所以默认值有效

print("----------------------------")
# key in dict
cities = {'BJ': 'Beijing', 'SH': 'Shanghai', 'GZ': 'Guangzhou', 'SZ': 'Shenzhen'}

if 'BJ' in cities:
    print('Beijing')  # True
else:
    print('No Beijing')
    
if 'HK' in cities:
    print('Hong Kong')
else:
    print('No Hong Kong')  # True
    
if 'CQ' not in cities:
    print('No CQ') # True
else:
    print('CQ')
    
print("----------------------------")
# dict.items()

cities = {'BJ': 'Beijing', 'SH': 'Shanghai', 'GZ': 'Guangzhou', 'SZ': 'Shenzhen'}

print ("Value :%s" % cities.items())

print("----------------------------")
# dict.setdefault(key, default=None)

personal_information_5 = {"name" : "yjs" , "age" : 18 , "height" : 1.6 , "is_single" : True}
print ("The gender of this boy is", personal_information_5.setdefault("gender", "male"))
print(personal_information_5)

print("----------------------------")

#dict.update(dict2)

personal_information_4 = {"name" : "yjs" , "age" : 18 , "height" : 1.6 , "is_single" : True}
print("The previous height of yjs is",personal_information_4.get("height"))

personal_information_4["height"] = 1.65
print("The present height of yjs is",personal_information_4.get("height"))

new_profile = {"name" : "yjs" , "age" : 20 , "height" : 1.69 , "is_single" : False}
personal_information_4.update(new_profile)
print("The new profile of yjs is",personal_information_4)

print("----------------------------")
# dict.values()

dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
print(keys)
values = dishes.values()
print(values)

n = 0
for val in values:
    n += val
print(n)

print(list(keys))
print(list(values))

# 视图对象是动态的，受字典变化的影响，以下删除了字典的 key，视图对象转为列表后也跟着变化

del dishes["eggs"]
del dishes["sausage"]
print(list(values))

print("----------------------------")
# pop(key[,default])
POTUS = {"First" : "George Washington", "Second" : "John Adams", "Third" : "Thomas Jefferson", "Fourth" : "James Madison"} 

POTUS_name = POTUS.pop("First")
print(POTUS_name)
print(POTUS)

# POTUS.pop("Fifth") KeyError: 'Fifth'
POTUS_NEW = POTUS.pop("Fifth","Unknown President") 
print(POTUS_NEW)