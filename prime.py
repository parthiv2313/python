n=int(input("Enter N:"))

if n%2!=0:
      for i in range(int(n/2)+1) :
           if n%1==0 :
              print(n,"Is not a Prime:")
              break

      else:
          print(n,"Is A Prime")

else:
    print(n,"Is Not A Prime")
