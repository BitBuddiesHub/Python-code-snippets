"""
while condition:
    statement_block
"""
n = 100
sum = 0
counter = 1
while counter <=n:
    sum = sum + counter
    counter += 1
    
print(sum)

counter_2 = 0
while True :
    print("smg love byx")
    counter_2 += 1
    if counter_2 == 100:
        break

counter_3 = 0
while counter_3 <= 100:
    print("SMG love byx",counter_3)
    counter_3 += 1
    
"""
while condition
"""

for i in range(10):
    print(i)
    
    
friends = ["smg","tkg","hkg","tg","gpg","yyg","nesg"]
for friend in friends:
    print(friend)
    
friends_name ="songyuxuan"
for letter in friends_name:
    print (letter)

for code in range(1,6,2):
    print(code)
    
for x in range(1,10):
    print(x)
    if x >= 5:
        break
else:
    print("the end")
    
print("---------------------")
    
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print("the end")

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print("the end")

