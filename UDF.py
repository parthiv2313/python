def oddeven(a):
    if a%2==0 :
        print(a," IS EVEN")
    else:
        print(a,"IS ODD")
def maxoftwo(a,b):
      if a>b  :
        print(a,"IS MAX")
      else :
        print (b, "IS MAX")
def maxofthree(a,b,c):
    if a>b :
        if a>c :
            print(a,"IS MAX")
        else :
            print(c,"IS MAX")
    elif b>c:
        print(b,"IS MAX")
    else :
        print(c,"IS MAX")
def fibonacci(n):
    a,b=0,1
    while b<n :
        print(b,end=" ")
        a,b=b,a+b
    print()
def prime(n) :
    if n%2!=0 :
        for i in range(3,int(n/2)+1,2) :
            if n%i==o :
                print(n,"IS NOT PRIME")
                break
            else :
              print(n,"IS PRIME")
    else:
         print(n,"IS NOT PRIME")
     
