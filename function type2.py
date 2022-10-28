#function
def name(a,b,c):
    print("the younger child name is:",a)

name(a='ram',b='tom',c='sita')

#arbitrary key word
def child(**args):
    print("name is:",args['lname'])

child(name='tom',lname='cruise',age=20,city='chennai')

#default parameter

def my_function(country = "Norway"):
    print("I am from" +country)

my_function()

#passing list as argument
def foodlist(a):
    for x in a:
        print(x)
list=[1,2,3,'a','b','c']
foodlist(list)

