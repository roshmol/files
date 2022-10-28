sub1=int(input("enter the first subject mark"))
sub2=int(input("enter the second subject mark"))
sub3=int(input("enter the Third subject mark"))
sub4=int(input("enter the four subject mark"))
sub5=int(input("enter the five subject mark"))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if(avg>=90):
    print("grade A")
elif((avg>=80)&(avg<90)):
    print("grade B")
elif ((avg>=70) & (avg<80)):
    print("grade C")
elif ((avg>=50) & (avg<70)):
    print("grade D")
else:
    print("grade F")