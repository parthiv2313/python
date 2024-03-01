import UDF

while True:
    print("*"*50)
    print("1. ODDEVEN")
    print("2. MAX OF TWO")
    print("3. MAX OF THREE")
    print("4. FIBONACCI")
    print("5. PRIME")
    print("6. EXIT")

    choice=int(input("Enter Your Choice : "))
    print("*"*50)

    if choice==1 :
               print("*"*50)
               a=int(input("ENter value "))
               
               UDF.oddeven(a)
    if choice==2 :
               print("*"*50)
               a=int(input("ENter value "))
               b=int(input("ENter value "))
               UDF.maxoftwo(a,b)
    if choice==3 :
               print("*"*50)
               a=int(input("ENter value "))
               b=int(input("ENter value "))
               c=int(input("ENter value "))
                
                
               UDF.maxofthree(a,b,c)
               
    if choice==4:
               print("*"*50)
               a=int(input("ENter value "))

               UDF.fibonacci(a)

    if choice==1:
               print("*"*50)
               a=int(input("ENter value "))
               
               UDF.prime(a)
    if choice==6:
                print("*"*50)
    
                print("Thank You")
    else :
        print("INVALID CHOICE [:(]")
