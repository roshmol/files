# f=open("txt.txt",mode="r")
# f.seek(3)
# print(f.tell())
# print(f.read())
# print(f.readline())
#
# f.close()

# f1=open("txt.txt",mode="w")
# f1.writelines("ros")
# f1.writelines("ram")
# f1.writelines("rash")
# f1.writelines("rish")
# f1.writelines("roy")
#
# f1.close()
#
# f2=open("txt.txt",mode="r")
# print(f2.read())
# f2.close()


# f=open("newtxt.txt","x")
# f.close()
# f3=open("newtxt.txt","w")
# f3.writelines("rish")
# f3.writelines("ram")
# f3.writelines("rash")
# f3.writelines("rish")
# f3.close()

# f4=open("newtxt.txt","r")
#


import os
# os.remove("newtxt.txt")
if os.path.exists("tem.txt"):
   os.remove()
else:
    print("there is no such file")

