'''
List is a group of different type of  datal like string numericals decimal boolean

'''
l=[1,2,3,1.1,"Python",10,True,1,2,False,"Coding"]

print(l)
l.append(100)
print(l)
l1=l.copy()
print(l1)
print(l.count(1))
l2=[1000,2000,3000]
l.extend(l2)
print(l)
print(l.index(10))
l.insert(5,101)
print(l)
l.pop()
print(l)
l.pop(5)
print(l)
l.remove(10)
print(l)
l.reverse()
print(l)

