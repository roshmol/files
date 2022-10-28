#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
#

#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such
#that is an integral number between 1 and n (both included). and then the program should print the
#dictionary.
#Suppose the following input is supplied to the program:
#8
def dictionaries(a):
    n2={}
    for i in range(1,n1+1):
        n2.update({i:i*i})
    print(n2)

n1=int(input("enter a number"))
dictionaries(n1)

