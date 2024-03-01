#Function With No Argument & No Return Value

def printline():
    print("*"*50)

printline()
print("Welcome")
printline()



#Function With Argument & No Return Value

def add(a,b):
    print("Addition",a+b)

printline()
x=int(input("Enter Value:"))
y=int(input("Enter Value:"))
add(x,y)




#Function With Argument &  Return Value

def sub(a,b):
   return a-b

printline()
x=int(input("Enter Value:"))
y=int(input("Enter Value:"))
print("Subtraction :",sub(x,y))
printline()
