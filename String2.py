s=input("String:")

al=0
sp=0
lc=0
uc=0
num=0

for i in s:
  if  i.isalpha():
      al=al+1
  elif i.isnumeric():
      num=num+1
  elif i.isspace():
      sp=sp+1
  if i.isupper():
      uc=uc+1
  elif i.islower():
      lc=lc+1

print("Alphabetics",al)
print("Numerical",num)
print("Spaces",sp)
print("Lowercases",lc)
print("Uppercase",uc)







