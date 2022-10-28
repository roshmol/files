#write a program to find lcm of a number using function
def lcmof_num(n1,n2):
    if(n1>n2):
        largest=n1
    else:
        largest=n2
    value=largest
    while(True):
        if(largest%n1==0 and largest%n2==0):
            print("lcm of the numbers:",largest)
            break
        else:
            largest=largest+value


n1=int(input("enter the first number"))
n2= int(input("enter the second number"))
lcmof_num(n1,n2)

#assign a different name to function using the name
def function():
    print("hello")
name=function
name()

#generate a python list of all the even numbers b/w 9to40 using function
def even(a):
    for i in range(4,9):
        if i%2==0:
            print(i)

n1=[]
even(n1)