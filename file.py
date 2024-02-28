print("***************************")
file=open("txt1","w")
file.write("This IS THE FIRST FILe")
file.close()
print("WRITTEN SUCCESSFULLY")

print("***************************")
file=open("txt1","r")
print(file.read())          
file.close()

print("***************************")
file=open("txt1","a")
file.write("\nThis IS THE APPENDED FILE")
file.close()
print("FILE APPENDED SUCCESSFULLY")

print("***************************")
file=open("txt1","r")
print(file.read())          
file.close()

print("***************************")
file=open("txt2","w+")
file.write("\nThis IS THE NEW FILE")
file.seek(0)
print(file.read())
file.close()

print("***************************")
                             
                             
