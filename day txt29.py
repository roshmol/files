a=int(input("enter the choice"))
if a==1:
    m="w"
elif a==2:
    m="a"
else:
    print("nothing")
f=open("txttxt.txt",mode=m)
while True:
    a=input("enter a line")
    f.writelines(a)
    f.writelines("\n")
    choice=input("continue y/n")
    if choice=="N":
        break

f.close()
