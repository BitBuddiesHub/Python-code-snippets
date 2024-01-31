set1 = {1,2,3,4,5}
print (set1)
set2 = {1,1,1,2,2,2,3,4,5,6,6}
print (set2)
print (len(set2))
list1 = [1,2,3,4,5,3,4,5,1,5,6,2,4,6,3,67,7,4,5,6,3,4,6,2,2,3,5]
print (set(list1))

for element in set2:
    print (element)
 
'''   
for i in range(0,len(set2)-1):
    print (set1[i]) # TypeError: 'set' object is not subscriptable
'''
set1 = {1,2,3,4,5}
set3 = {1,3,5}

# 交集
print (set1 & set3)
print (set1.intersection(set3))

# 并集
print (set1 | set3)
print (set1.union(set3))

# 差集
print (set1 - set3)
print (set1.difference(set3))

# 对称差
print (set1 ^ set3)

print(set3 < set1)
print(set3 <= set1)
print(set1.issubset(set3))
print(set1.issuperset(set3))

setsmg = {'smg'}

setsmg.add('byx')
print(setsmg)

setsmg.add('004')
print(setsmg)

setsmg.remove('004')
print(setsmg)
setsmg.discard('byx')
print(setsmg)
# setsmg.remove('004') # KeyError: '004'
setsmg.discard('byx')

setsmg.clear()
print(setsmg)

setsmg = frozenset({'smg','004','byx'})
# setsmg.remove('byx') # AttributeError: 'frozenset' object has no attribute 'remove'
# setsmg.discard('004') # AttributeError: 'frozenset' object has no attribute 'discard'
# setsmg.clear() # AttributeError: 'frozenset' object has no attribute 'clear'