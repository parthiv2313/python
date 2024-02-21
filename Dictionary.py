d={777:"Parthiv",666:"Darsh",555:"Zayn",444:"SRK"}

print(d)
print(d[777])
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(666))
print(d)
d1={333:"Tripti"}
d.update(d1)
print(d)
d.popitem()
print(d)

for i in d:
    print(i," : ",d[i])
