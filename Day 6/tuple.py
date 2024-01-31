tup1 = (1,2,3,4,5)
tup2 = ('smg','yjs','cyq','byx','qhw','zwz')
tup3 = "a","b","c","d"
print(type(tup1))
print(type(tup2))
print(type(tup3))

tup4 = (1)
tup5 = (1,)
print(type(tup4))
print(type(tup5))

print (tup2[2])

print (tup2[-1])

print (tup2[1:3])

print (tup1 + tup2)

# tup1[0] = 10

# del tup1

print(len(tup2))

for i in tup1:
    print(i)
    
print (tup1 * 4)

max(tup1)
min(tup1)
list = ['a','b','c']
tup6 = tuple(list)